import os
def rename_file(file_path, new_name):
    os.rename(file_path, new_name)

file_path = input("Enter the path of the file you want to rename: ")
new_name = input("Enter the new name for the file: ")
rename_file(file_path, new_name)
print("File renamed successfully.")