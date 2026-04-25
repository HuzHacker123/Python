f = open ("poem.txt", "rt")
data = f.read()
if "twinkle" in data:
    print("Yes, 'twinkle' is present.")
else:
    print("No, 'twinkle' is not present.")
f.close()