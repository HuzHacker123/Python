tuple=("10,9,8,7,6,5,4,3,2,1")
print(tuple)
tuple.sort()  # This will raise an AttributeError since tuples are immutable
print(tuple)