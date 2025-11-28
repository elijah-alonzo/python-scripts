import os
from PIL import Image
import sys

def resize_images(folder, width, height):
    for filename in os.listdir(folder):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            path = os.path.join(folder, filename)
            img = Image.open(path)
            img = img.resize((width, height))
            img.save(os.path.join(folder, f"resized_{filename}"))
            print(f"Resized {filename}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python image_resizer.py <folder> <width> <height>")
    else:
        resize_images(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
