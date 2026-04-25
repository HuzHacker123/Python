a=list(input("Enter 4 numbers: ").split())
if a[0]>a[1] and a[0]>a[2] and a[0]>a[3]:
    print(a[0],"is the greatest number")
elif a[1]>a[2] and a[1]>a[3]:
    print(a[1],"is the greatest number")
elif a[2]>a[3]:
    print(a[2],"is the greatest number")
else:
    print(a[3],"is the greatest number")