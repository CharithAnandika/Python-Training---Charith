import os
import shutil

source_file = "source_doc.txt"
with open(source_file, "w") as f:
    f.write("this is original content.")
print(f"Created '{source_file}' for copying.")

# Copy the file
destination_file = "copied_doc.txt"
try:
    shutil.copy(source_file, destination_file)
    print(f"'{source_file}' copied to '{destination_file}' successfully.")

    with open(destination_file, "r") as f:
        content = f.read()
    print(f"Content of '{destination_file}': '{content}'")

except FileNotFoundError:
    print(f"Error: Source file '{source_file}' not found.")
