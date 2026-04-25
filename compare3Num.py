def compare_three_numbers(a, b, c):
    if a>b and a>c:
        return f"{a} is the largest number."
    if b>c:
        return f"{b} is the largest number."
    return f"{c} is the largest number."
print(compare_three_numbers(10, 20, 15)) 
