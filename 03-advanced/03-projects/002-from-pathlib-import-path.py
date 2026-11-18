from pathlib import Path
import shutil
source_path=Path(r"D:/into/doc")
destination_path=Path(r"D:/into/doc2")

file_category={"document":[".doc",".docx",".pdf",".txt"],
               "image":[".jpg",".jpeg",".png",".gif"],"excel":[".xls",".xlsx"],
               "video":[".mp4",".mkv",".avi"],"audio":[".mp3",".wav"],"archive":[".zip",".rar",".tar",".gz"],"sounds":[".mp3",".wav"]
             "excel":[".xls",".xlsx"],"video":[".mp4",".mkv",".avi"],"audio":[".mp3",".wav"],"archive":[".zip",".rar",".tar",".gz"],"sounds":[".mp3",".wav"]   }
def create_parant_folder(path):
    if not destination_path.exists():
        destination_path.mkdir(parents=True,exist_ok=True)
 def search_file(path):
    for file in path.iterdir():
        if file.is_file():
            file_ext=file.suffix.lower()
            for category,extensions in file_category.items():
                if file_ext in extensions:
                    category_folder=destination_path/category
                    create_parant_folder(category_folder)
                    shutil.move(str(file),str(category_folder/file.name))
                    break
        elif file.is_dir():
            search_file(file)
            
