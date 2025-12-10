try:

    # Take user input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Display original values
    print("\n--- Original Values ---")
    print(f"Number 1: {num1}")
    print(f"Number 2: {num2}")

    # Swap without temporary variable using tuple unpacking
    num1, num2 = num2, num1

    #using temporary variable
    # temp = num1   
    # num1 = num2
    # num2 = temp
    

    # Display swapped values
    print("\n--- Swapped Values ---")
    print(f"Number 1: {num1}")
    print(f"Number 2: {num2}")

except ValueError:
    print("Invalid input. Please enter numeric values.")