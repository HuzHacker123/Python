Name=input("Enter your name: ")
Date=input("Enter the date (DD/MM/YYYY): ")

letter='''Dear {Name},
You are selected!
{Date}'''
print(letter)
print("\n")
print(letter.format(Name=Name, Date=Date))