def Higer(fx, x):
    return 10 + fx(x)
def print_h(fx,fy,fz,x,y):
    return fx(x) + fy(x) + fz(x,y)


square = lambda x: x**2
cube = lambda x: x**3
sum = lambda x, y: x + y

print(Higer(lambda x: x * x, 5)) # Output will be 35

print(print_h(square, cube, sum, 2, 3)) # This demonstrates passing multiple lambda functions as arguments
