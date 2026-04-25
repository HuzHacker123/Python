import os

os.mkdir("Tables for 13yrs old")
for num in range(2, 21):
    with open(f"Tables for 13yrs old/Table_of_{num}.txt", "w") as file:
        for i in range(1, 11):
            file.write(f"{num} x {i} = {num * i}\n")