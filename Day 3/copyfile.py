import os

source_file = "source_doc.txt"
with open(source_file, "w") as f:
    f.write("this is original content.")
print(f"created '{source_file}' for copying.")

#copy the file
destination_file = "copied_doc.txt"
try : 
    shutil.copy(source_file,destination_file)
    print(f"'{source_file}' copied to '{destination_file}' successfully.")
    print(f"contect of '{destination_file}' : '{open(destination_file)}' ")

except FileExistsError:
    print(f"error : source file '{source_file}' not found")