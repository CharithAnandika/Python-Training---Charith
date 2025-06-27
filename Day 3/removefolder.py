import os

new_folder_name = "my_new_folder"

try:
    os.mkdir(new_folder_name)
    print(f"Directory '{new_folder_name} created successfully")

except FileExistsError:
    print(f"Directory '{new_folder_name} already exists")

os.rmdir(new_folder_name)
print(f"Directory '{new_folder_name} removed successfully") 