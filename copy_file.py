import os
def copy_file(source_file, destination_file):
    with open(source_file, "r") as f:
        content = f.read()
    with open(destination_file, "w") as g:
        g.write(content)

copy_file("Donkey.txt", "Donkey02.txt")

if os.path.exists("Donkey02.txt"):
    print("File copied successfully.")
else:
    print("File copy failed.")