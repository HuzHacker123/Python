str=input("Enter a string: ")
print("Reversed string is:",str[::-1])

for i in range(len(str)-1,-1,-1):
    print(str[i],end="")