try:
    # Take user input
    n = int(input("Enter the value of N: "))
    
    # Validate input
    if n <= 0:
        print("Please enter a positive number.")
    else:
        # Display the series of perfect squares (excluding multiples of 4)
        print(f"\nSeries of perfect squares up to {n}:")
        i = 1
        while i * i <= n:
            # Check if i is not a multiple of 4
            if i % 4 != 0:
                print(i * i, end=" ")
            i += 1
        print()  # New line after series

except ValueError:
    print("Invalid input. Please enter a valid integer.")