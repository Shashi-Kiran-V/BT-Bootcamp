try:
    # Take user input
    n = int(input("Enter the value of N: "))
    
    # Validate input
    if n <= 0:
        print("Please enter a positive number.")
    else:
        # Display series from 1 to N
        print(f"\nSeries from 1 to {n}:")
        for i in range(1, n + 1):
            print(i, end=" ")
        print()  # New line after series

except ValueError:
    print("Invalid input. Please enter a valid integer.")