try:
    # Take user input
    n = int(input("Enter the number of rows: "))
    
    # Validate input
    if n <= 0:
        print("Please enter a positive number.")
    else:
        # Print star pattern
        print(f"\nStar pattern with {n} rows:")
        for i in range(n):
            for j in range(n):
                print("*", end="")
            print()  # New line after each row

except ValueError:
    print("Invalid input. Please enter a valid integer.")