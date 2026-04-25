def sum_natural_numbers(n):
    if n == 1:
        return 1
    elif n < 1:
        return "Invalid input, please enter a natural number."
    else:
        return n + sum_natural_numbers(n - 1)
n=int(input("Enter a Natural number: "))
print("The sum of first",n,"natural numbers is:",sum_natural_numbers(n))