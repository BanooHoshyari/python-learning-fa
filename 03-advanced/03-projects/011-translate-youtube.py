#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
YouTube EN->FA Translator
-------------------------
- Downloads audio from a YouTube URL
- Transcribes English speech with Faster-Whisper
- Translates to Persian (FA) using Argos Translate (offline)
- Exports English and Persian .srt subtitle files (+ plain .txt)
Optional: shows an ffmpeg command to burn Persian subtitles into the video.

Usage:
    python translate_youtube.py --url "https://www.youtube.com/watch?v=..." --model small --outdir outputs

Notes:
- First run will auto-download the Argos EN->FA package.
- Install ffmpeg on your system if you want to burn subtitles into the video.
- If GPU is available, set --device cuda for speed.
"""

import argparse
import os
import re
import sys
import tempfile
import subprocess
from datetime import timedelta

# yt-dlp for download
import yt_dlp

# faster-whisper for transcription
from faster_whisper import WhisperModel

# argos-translate for offline machine translation
import argostranslate.package
import argostranslate.translate


def srt_timestamp(seconds: float) -> str:
    if seconds < 0:
        seconds = 0
    td = timedelta(seconds=seconds)
    # SRT format: HH:MM:SS,mmm
    total_seconds = int(td.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    secs = total_seconds % 60
    millis = int((td.total_seconds() - total_seconds) * 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"


def write_srt(segments, path, translate_fn=None):
    with open(path, "w", encoding="utf-8") as f:
        for i, seg in enumerate(segments, start=1):
            text = seg["text"]
            if translate_fn:
                text = translate_fn(text)
            f.write(str(i) + "\n")
            f.write(srt_timestamp(seg["start"]) + " --> " + srt_timestamp(seg["end"]) + "\n")
            f.write(text.strip() + "\n\n")


def write_txt(segments, path, translate_fn=None):
    with open(path, "w", encoding="utf-8") as f:
        for seg in segments:
            text = seg["text"]
            if translate_fn:
                text = translate_fn(text)
            f.write(text.strip() + "\n")


def ensure_argos_en_fa():
    """
    Ensures Argos Translate has an English->Persian model installed.
    Downloads it if missing.
    """
    # Refresh package index
    argostranslate.package.update_package_index()
    available_packages = argostranslate.package.get_available_packages()
    installed_packages = argostranslate.package.get_installed_packages()

    # language codes: "en" -> English, "fa" -> Persian
    need = [p for p in available_packages if p.from_code == "en" and p.to_code == "fa"]

    if not need:
        print("No Argos EN->FA package found in index. Exiting.", file=sys.stderr)
        sys.exit(1)

    have_en_fa = any(p.from_code == "en" and p.to_code == "fa" for p in installed_packages)

    if not have_en_fa:
        # Choose the largest (usually latest/best) package
        pkg = sorted(need, key=lambda p: p.size, reverse=True)[0]
        print(f"Downloading Argos EN->FA package: {pkg} (size ~{pkg.size/1e6:.1f} MB)")
        download_path = pkg.download()
        argostranslate.package.install_from_path(download_path)

    # Load translators
    argostranslate.translate.load_installed_packages()
    translators = argostranslate.translate.get_installed_languages()
    en_lang = next((l for l in translators if l.code == "en"), None)
    fa_lang = next((l for l in translators if l.code == "fa"), None)
    if not en_lang or not fa_lang:
        print("Failed to load EN/FA languages after install.", file=sys.stderr)
        sys.exit(1)
    return en_lang.get_translation(fa_lang)


def download_audio(url: str, outdir: str) -> dict:
    """
    Downloads best audio and the full video (for optional burning) using yt-dlp.
    Returns dict with paths: {"audio": ..., "video": ...}
    """
    os.makedirs(outdir, exist_ok=True)
    ydl_opts_audio = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(outdir, "%(title)s.%(ext)s"),
        "postprocessors": [{"key": "FFmpegExtractAudio", "preferredcodec": "mp3", "preferredquality": "192"}],
        "quiet": True,
        "noprogress": True,
    }
    ydl_opts_video = {
        "format": "bestvideo*+bestaudio/best",
        "outtmpl": os.path.join(outdir, "%(title)s.%(ext)s"),
        "quiet": True,
        "noprogress": True,
    }

    print("Downloading audio...")
    audio_path = None
    with yt_dlp.YoutubeDL(ydl_opts_audio) as ydl:
        info = ydl.extract_info(url, download=True)
        base = ydl.prepare_filename(info)
        audio_path = os.path.splitext(base)[0] + ".mp3"

    print("Downloading full video (optional for burning subs)...")
    video_path = None
    with yt_dlp.YoutubeDL(ydl_opts_video) as ydl:
        info = ydl.extract_info(url, download=True)
        video_path = ydl.prepare_filename(info)

    return {"audio": audio_path, "video": video_path}


def transcribe(audio_path: str, model_size: str = "small", device: str = "auto", compute_type: str = "int8"):
    """
    Transcribe audio with Faster-Whisper.
    Returns list of segments: [{"start": float, "end": float, "text": str}, ...]
    """
    if device == "auto":
        # Heuristic: if CUDA visible, try cuda
        device = "cuda" if os.environ.get("CUDA_VISIBLE_DEVICES", "") not in ("", "-1") else "cpu"

    print(f"Loading Whisper model: {model_size} on {device} ({compute_type}) ...")
    model = WhisperModel(model_size, device=device, compute_type=compute_type)
    segments, info = model.transcribe(audio_path, language="en", vad_filter=True)
    segs = []
    for s in segments:
        segs.append({"start": s.start, "end": s.end, "text": s.text})
    return segs


def main():
    parser = argparse.ArgumentParser(description="Translate a YouTube video from English to Persian (FA).")
    parser.add_argument("--url", required=True, help="YouTube URL")
    parser.add_argument("--outdir", default="outputs", help="Output directory")
    parser.add_argument("--model", default="small", help="Whisper model size: tiny/base/small/medium/large-v3")
    parser.add_argument("--device", default="auto", help="cpu or cuda (or auto)")
    parser.add_argument("--compute-type", default="int8", help="int8, int8_float16, float16, float32 (depends on device)")
    args = parser.parse_args()

    os.makedirs(args.outdir, exist_ok=True)

    # 1) Download
    paths = download_audio(args.url, args.outdir)
    audio_path = paths["audio"]
    video_path = paths["video"]
    print(f"Audio: {audio_path}")
    print(f"Video: {video_path}")

    # 2) Transcribe EN
    segments = transcribe(audio_path, model_size=args.model, device=args.device, compute_type=args.compute_type)

    # 3) Setup translator EN->FA
    print("Preparing Argos EN->FA translator (first run may take a while)...")
    translator = ensure_argos_en_fa()
    translate_fn = translator.translate

    # 4) Write outputs
    base = os.path.splitext(os.path.basename(video_path or audio_path))[0]
    en_srt = os.path.join(args.outdir, f"{base}.en.srt")
    fa_srt = os.path.join(args.outdir, f"{base}.fa.srt")
    en_txt = os.path.join(args.outdir, f"{base}.en.txt")
    fa_txt = os.path.join(args.outdir, f"{base}.fa.txt")

    print("Saving subtitles and transcripts...")
    write_srt(segments, en_srt, translate_fn=None)
    write_srt(segments, fa_srt, translate_fn=translate_fn)
    write_txt(segments, en_txt, translate_fn=None)
    write_txt(segments, fa_txt, translate_fn=translate_fn)

    print("\nDone! Files created:")
    print(" -", en_srt)
    print(" -", fa_srt, "(Persian subtitles)")
    print(" -", en_txt)
    print(" -", fa_txt, "(Persian transcript)")

    print("\n(Optional) Burn Persian subtitles into the video using ffmpeg:")
    print(f'  ffmpeg -i "{video_path}" -vf "subtitles={fa_srt}" -c:a copy "{base}.fa.hardsub.mp4"')

if __name__ == "__main__":
    main()
