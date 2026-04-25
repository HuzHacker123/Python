import os

def identical_file(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        return f1.read() == f2.read()
    
if identical_file("Donkey.txt", "Donkey02.txt"):
    print("The files are identical.")
else:
    print("The files are not identical.")
