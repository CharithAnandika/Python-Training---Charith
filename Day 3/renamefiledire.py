import os

old_name = "old_file.txt"
new_name = "new_file.txt"

with open(old_name, 'w') as f:
    f.write("content of old file")

try:
    os.rename(old_name,new_name)
    print(f"renamed '{old_name}' to '{new_name}'.")
except:
    print(f"'{old_name}' does not exist")