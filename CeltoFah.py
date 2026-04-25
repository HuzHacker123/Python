def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
n=float(input("Enter temperature in Celsius: "))
print(celsius_to_fahrenheit(n))