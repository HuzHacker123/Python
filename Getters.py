class MyClass:
    def __init__(self, value):
        self._value = value
    @property
    def value(self):
        return self._value
    
obj = MyClass(21)
print(obj.value)