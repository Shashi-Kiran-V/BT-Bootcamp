try:
    # Take user input
    n = int(input("Enter the number of rows: "))
    
    # Validate input
    if n <= 0:
        print("Please enter a positive number.")
    else:
        # Print number pattern
        print(f"\nNumber pattern with {n} rows:")
        for i in range(1, n + 1):
            for j in range(1, 6):
                print(j, end="")
            print()  # New line after each row

except ValueError:
    print("Invalid input. Please enter a valid integer.")