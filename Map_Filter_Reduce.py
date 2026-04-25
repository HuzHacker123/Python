l = [3, 6, 8, 2, 5, 10, 7, 4, 9, 1]

# Using map to double each element in the list
mapped = map(lambda x: x * 2, l)
print(list(mapped))

# Using filter to get only even numbers from the list
filtered = filter(lambda x: x > 3, l)
print(list(filtered))

# Using reduce to calculate the sum of all elements in the list
from functools import reduce
reduced = reduce(lambda x, y: x + y, l)
print(reduced)