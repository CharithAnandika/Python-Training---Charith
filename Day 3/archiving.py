import shutil
import os

# Setup: create dummy directory
data_folder = "my_data_for_archive"
os.makedirs(os.path.join(data_folder, "docs"), exist_ok=True)

with open(os.path.join(data_folder, "important.txt"), "w") as f:
    f.write("important data here")

with open(os.path.join(data_folder, "docs", "notes.md"), "w") as f:
    f.write("#meeting notes")

print(f"Created dummy folder for archiving: '{data_folder}'.")

archive_name = "my_data_archive"

try:
    archive_path = shutil.make_archive(archive_name, 'zip', root_dir=data_folder)
    print(f"Archive created: '{archive_path}'")
    print(f"Does archive exist? {os.path.exists(archive_path)}")
except Exception as e:
    print(f"Error occurred: {e}")
