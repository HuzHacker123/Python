class MyClass:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

class MyChildClass(MyClass):
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Country: {self.country}")
        print()

obj = MyChildClass("Huzefa", 21, "India")
obj.display()