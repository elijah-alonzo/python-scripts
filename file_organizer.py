import os
import shutil

# Set the directory you want to organize
TARGET_DIR = "."

FILE_TYPES = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".csv"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Audio": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".7z"],
    "Scripts": [".py", ".js", ".sh"]
}

def organize_files():
    for file in os.listdir(TARGET_DIR):
        file_path = os.path.join(TARGET_DIR, file)

        if os.path.isdir(file_path):
            continue

        _, ext = os.path.splitext(file)
        moved = False

        for folder, extensions in FILE_TYPES.items():
            if ext.lower() in extensions:
                folder_path = os.path.join(TARGET_DIR, folder)
                os.makedirs(folder_path, exist_ok=True)
                shutil.move(file_path, os.path.join(folder_path, file))
                print(f"Moved {file} → {folder}/")
                moved = True
                break

        if not moved and ext:
            folder_path = os.path.join(TARGET_DIR, "Others")
            os.makedirs(folder_path, exist_ok=True)
            shutil.move(file_path, os.path.join(folder_path, file))
            print(f"Moved {file} → Others/")

if __name__ == "__main__":
    organize_files()
