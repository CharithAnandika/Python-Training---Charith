import os

path_component = "C:\\Python Training - Charith"
path_component1 = "Day 3"
file_name = "new.pdf"

full_path = os.path.join(path_component,path_component1,file_name)
print(f"joined path : {full_path}")
