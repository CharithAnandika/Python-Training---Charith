import os

full_path = "C:\Python Training - Charith"

directory_name = os.path.dirname(full_path)
basename = os.path.basename(full_path)

print(f"Directtory name : {directory_name}")
print(f"Basename : {basename}")
