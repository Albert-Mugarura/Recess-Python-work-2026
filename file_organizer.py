import os, shutil

path = input("Enter downloads folder path: ")

cats = {
    "Images": [".jpg",".jpeg",".png",".gif"],
    "Documents": [".pdf",".docx",".txt",".xlsx"],
    "Videos": [".mp4",".avi",".mkv"],
    "Archives": [".zip",".rar",".7z"],
    "Audio": [".mp3",".wav"],
}

for f in os.listdir(path):
    fp = os.path.join(path, f)
    if os.path.isfile(fp):
        ext = os.path.splitext(f)[1].lower()
        for folder, exts in cats.items():
            if ext in exts:
                dst = os.path.join(path, folder)
                os.makedirs(dst, exist_ok=True)
                shutil.move(fp, os.path.join(dst, f))
                print(f"Moved {f} -> {folder}")
                break
