try:
    # Take user input
    n = int(input("Enter the number of rows: "))
    
    # Validate input
    if n <= 0:
        print("Please enter a positive number.")
    else:
        # Print Fibonacci series pattern
        print(f"\nFibonacci series pattern with {n} rows:")
        
        # Initialize first two Fibonacci numbers
        a, b = 1, 1
        
        for i in range(1, n + 1):
            for j in range(i):
                print(a, end=" ")
                # Generate next Fibonacci number
                a, b = b, a + b
            print()  # New line after each row

except ValueError:
    print("Invalid input. Please enter a valid integer.")