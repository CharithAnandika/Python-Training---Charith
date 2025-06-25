import os

path = "C:\\Python Training - Charith\\new.txt"
path1 = "C:\\Python Training - Charith"
path2 = "non_existing_path"

print(f"'{path}' is a file: {os.path.isfile(path)}")
print(f"'{path}' is a directory: {os.path.isdir(path)}")

print(f"'{path1}' is a file: {os.path.isfile(path1)}")
print(f"'{path1}' is a directory: {os.path.isdir(path1)}")

print(f"'{path2}' is a file: {os.path.isfile(path2)}")
print(f"'{path2}' is a directory: {os.path.isdir(path2)}")