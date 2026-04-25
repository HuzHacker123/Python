a={}
print(type(a))
for i in range(4):
    Name=input("Enter Your Name:")
    Lang=input("Enter Your Favourite Programming Language:")
    a.update({Name:Lang})
print(a)