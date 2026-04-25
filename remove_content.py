import os
def remove_content(file_path):
    with open(file_path, 'w'):
        pass

remove_content("Donkey02.txt")
print("Content removed successfully.")