import shutil
from pathlib import Path

source_dir = Path(r"D:\intoe\doc")

if not source_dir.exists():
    raise FileNotFoundError(f"مسیر پیدا نشد: {source_dir}")

for item in source_dir.iterdir():
    if item.is_file():
        ext = item.suffix.lower().lstrip(".")  # مثلا: pdf, jpg, py
        folder_name = ext if ext else "other"

        target_dir = source_dir / folder_name
        target_dir.mkdir(exist_ok=True)

        target_file = target_dir / item.name
        counter = 1

        while target_file.exists():
            new_name = f"{item.stem}_{counter}{item.suffix}"
            target_file = target_dir / new_name
            counter += 1

        shutil.move(str(item), str(target_file))
        print(f"Moved: {item.name} -> {target_file}")

print("دسته‌بندی فایل‌ها کامل شد.")