try:
    # Take user input
    n = int(input("Enter the value of N: "))
    
    # Validate input
    if n <= 0:
        print("Please enter a positive number.")
    else:
        # Display series of squares of even numbers
        print(f"\nSeries of squares of even numbers up to {n}:")
        i = 2
        while i * i <= n:
            print(i * i, end=" ")
            i += 2
        print()  # New line after series

except ValueError:
    print("Invalid input. Please enter a valid integer.")