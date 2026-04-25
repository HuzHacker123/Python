import os

f = open("a_example.txt", "x")
f.close()

f = open("a_example.txt", "w")
f.write("Hello, World!\n")
f.write("This is a test file.\n")
f.write("Goodbye!\n")
f.close()

f = open("a_example.txt", "r")
content = f.read()
print(content)
f.close()

f = open("a_example.txt", "w")
f.write("Line 1\n")
f.write("Line 2\n")
f.write("Line 3\n")
f.close()

f = open("a_example.txt", "r")
while True:
    lines = f.readlines()
    if not lines:
        break
    for line in lines:
        print(line.strip())
f.close()