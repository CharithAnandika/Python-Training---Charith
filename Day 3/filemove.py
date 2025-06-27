import shutil
import os

file_to_move = "report.pdf"
target_dir = "archives"

with open(file_to_move,"w") as f:
    f.write("confidential report data")
os.makedirs(target_dir, exist_ok =True)
print(f"Created '{file_to_move}' and '{target_dir}'.")

#move the file

try :
    shutil.move(file_to_move,target_dir)
    print(f"'{file_to_move}' moved to '{target_dir}' successfully.")
    print(f"new path: {os.path.join(target_dir, file_to_move)}")

except:
    print(f"Error : soure file '{file_to_move}' not found.")
