try:
    # Take user input
    n = int(input("Enter the value of N: "))
    
    # Validate input
    if n <= 0:
        print("Please enter a positive number.")
    else:
        # Display the Fibonacci series
        print(f"\nFibonacci series up to {n}:")
        a, b = 1, 1
        
        while a <= n:
            print(a, end=" ")
            a, b = b, a + b
        print()  # New line after series

except ValueError:
    print("Invalid input. Please enter a valid integer.")