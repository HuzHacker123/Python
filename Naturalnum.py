n=int(input("Enter a Natural number: "))
sum=0
i=1
if n>0:
    while i in range(i,n+1):
        sum=i+sum
        i+=1
    print(f"The sum of first {n} natural numbers is: {sum}")
else:
    print("Please enter a valid natural number")