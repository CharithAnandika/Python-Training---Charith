import pathlib

print("1. Creating path object")

#print(pathlib.path)
current_dir = pathlib.Path.cwd()
print(f"current working dir : {current_dir}")

#relative path
relative_file = pathlib.Path('my_document.txt')
print(f" relative path : {relative_file}")

joined_path = current_dir/'data'/'report'/'report.csv'

#Accessing path components
print(f"full path : {joined_path}")
print(f"file name : {joined_path.name}")
print(f"Parent directory : {joined_path.parent}")
print(f"File stem : {joined_path.stem}")
print(f"File suffix : {joined_path.suffix}")
print(f"All suffix : {joined_path.suffixes}")
print(f"anchor : {joined_path.anchor}")
print(f"path parts: {joined_path.parts}") 