def inch_to_cms(inch):
    """Convert inches to centimeters."""
    cms = inch * 2.54
    return cms
inch=int(input("Enter length in inches: "))
print(f"{inch} inches is equal to {inch_to_cms(inch)} centimeters.")