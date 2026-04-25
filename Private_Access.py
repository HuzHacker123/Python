class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

obj = Student("Huzefa", 21)
print(obj._Student__name) # private access
print(obj.__name) # this will throw an error
print(obj.__age)
