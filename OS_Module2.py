import os
os.getcwd()  # Get the current working directory
print(os.listdir('.'))  # List all files and directories in the current directory
os.mkdir("Path") # Create a directory named "Path"
os.rmdir("Path") # Remove the directory named "Path"
os.mkdir("new_directory")  # Create a new directory named "new_directory"
os.rename("new_directory", "Days")  # Rename a directory from "new_directory" to "Days"
print(os.path.exists("Days"))  # Check if "Days" directory exists
# os.chdir("Days")  # Change the current working directory to "Days"
for i in range(1,101):
    os.mkdir(f"Days/Day{i}")

for i in range(1,101):
    os.rename(f"Days/Day{i}",f"Days/Day {i}")

for i in range(1,101):
    os.rmdir(f"Days/Day {i}")

os.rmdir("Days")  # Remove the "Days" directory
