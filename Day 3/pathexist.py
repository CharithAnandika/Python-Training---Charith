import os

path_to_check_file = "C:\\Python Training - Charith\\new.txt"
path_to_check_dir = "C:\\Python Training - Charith"

with open(path_to_check_file, 'w') as f:
    f.write("hello1234")
os.makedirs(path_to_check_dir, exist_ok = True)

if os.path.exists(path_to_check_file):
    print(f"'{path_to_check_file}' exists.")
else :
    print(f"'{path_to_check_file}' does not exists.")

if os.path.exists(path_to_check_dir):
    print(f"'{path_to_check_dir}' exists.")
else :
    print(f"'{path_to_check_dir}' does not exists.")


