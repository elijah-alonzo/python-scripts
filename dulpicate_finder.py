import os
import hashlib

TARGET_DIR = "."

def hash_file(path):
    hash_md5 = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def find_duplicates():
    hashes = {}
    duplicates = []

    for root, _, files in os.walk(TARGET_DIR):
        for file in files:
            full_path = os.path.join(root, file)
            file_hash = hash_file(full_path)

            if file_hash in hashes:
                duplicates.append((full_path, hashes[file_hash]))
            else:
                hashes[file_hash] = full_path

    if duplicates:
        print("Duplicate Files Found:")
        for dup, original in duplicates:
            print(f"{dup}  ← duplicate of  {original}")
    else:
        print("No duplicates found.")

if __name__ == "__main__":
    find_duplicates()
