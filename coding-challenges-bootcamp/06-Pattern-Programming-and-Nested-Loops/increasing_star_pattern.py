try:
    # Take user input
    n = int(input("Enter the number of rows: "))
    
    # Validate input
    if n <= 0:
        print("Please enter a positive number.")
    else:
        # Print increasing star pattern
        print(f"\nIncreasing star pattern with {n} rows:")
        for i in range(1, n + 1):
            for j in range(i):
                print("*", end="")
            print()  # New line after each row

except ValueError:
    print("Invalid input. Please enter a valid integer.")