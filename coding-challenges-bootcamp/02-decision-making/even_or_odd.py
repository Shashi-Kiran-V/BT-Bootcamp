try:
    # Take user input
    num = int(input("Enter a number: "))

    # Check if number is even or odd
    if num % 2 == 0:
        print(f"\n{num} is an EVEN number")
    else:
        print(f"\n{num} is an ODD number")

except ValueError:
    print("Invalid input. Please enter a valid integer.")