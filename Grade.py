Marks=list(input("Enter the marks separated by commas: ").split(","))
percent=(int(Marks[0])+int(Marks[1])+int(Marks[2])+int(Marks[3])+int(Marks[4]))/5
if percent>=90:
    print("Grade Ex")
elif percent>=80:
    print("Grade A")
elif percent>=70:
    print("Grade B")
elif percent>=60:
    print("Grade C")
elif percent>=50:
    print("Grade D")
else:
    print("Grade F")