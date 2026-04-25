class MyClass:
    def __init__(self, Name, Age, Country):
        self.Name = Name
        self.Age = Age
        self.Country = Country
        print(f"Name: {self.Name}\nAge: {self.Age}\nCountry: {self.Country}")
        print()
MyClass("Alice", 30, "USA")
MyClass("Bob", 25, "Canada")
MyClass("Charlie", 35, "UK")
MyClass("Diana", 28, "Australia")
MyClass("Ethan", 40, "Germany")