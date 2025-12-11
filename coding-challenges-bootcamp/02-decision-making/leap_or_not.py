try:
    # Take user input
    year = int(input("Enter a year: "))

    # Check if it's a leap year
    # A year is a leap year if:
    # 1. It is divisible by 4 AND not divisible by 100
    # OR
    # 2. It is divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"\n{year} is a LEAP YEAR")
    else:
        print(f"\n{year} is NOT a LEAP YEAR")

except ValueError:
    print("Invalid input. Please enter a valid year.")