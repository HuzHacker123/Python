import os

f = open("a_example.txt", "x")
f.close()

f = open("a_example.txt", "w")
f.write("Hello, World!")
f.close()

f = open("a_example.txt", "r")
content = f.read()
print(content)
f.close()

f= open("a_example.txt", "w")
f.write("Hello, Huzefa!")
f.close()

f = open("a_example.txt", "r")
content = f.read()
print(content)
f.close()

f = open("a_example.txt", "a")
f.write(", How are you?")
f.close()

with open("a_example.txt", "r") as f:
    print(f.read())

os.remove("a_example.txt")