def greet(fx):
    def mfx(*args, **kwargs):
        print("Hello! Welcome to the Decorators module.")
        fx(*args, **kwargs)
        print("Decorators allow you to modify the behavior of functions or methods.")
    return mfx

@greet
def huzefa():
    print("This is the main function being decorated.")

@greet
def add(a, b):
    print(a + b)

huzefa()
add(5, 10)