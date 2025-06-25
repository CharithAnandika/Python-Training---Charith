import os

new_directory = "./temp"

if os.path.exists(new_directory) and os.path.isdir(new_directory):
    os.chdir(new_directory) #change dir
    print(f"changed directory to : {os.getcwd()}")
else:
    print(f"directory '{new_directory}' does not exist")