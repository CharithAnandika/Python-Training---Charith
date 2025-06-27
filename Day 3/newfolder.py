import os

new_folder_name = "Day 4"

try:
    os.mkdir(new_folder_name)
    print(f"Directory '{new_folder_name} created successfully")

except FileExistsError:
    print(f"Directory '{new_folder_name} already exists")
