with open("a_example.txt", 'w') as f:
    f.write("This is an example file. It contains some text for testing seek, tell, and truncate methods.")

with open("a_example.txt", 'r') as f:
    print(f.tell())  # Get the current cursor position
    
    f.seek(10)  # Move the cursor to the 10th byte
    
    print(f.tell())  # Get the new cursor position

    data = f.read(82)  # Read 20 bytes from the current cursor position
    print("Data read from position 10:", data)

with open("a_example.txt", 'w') as f:
    f.truncate(1)  # Truncate the file to 1 byte

with open("a_example.txt", 'r') as f:
    content = f.read()
    print("Content after truncation:", content)