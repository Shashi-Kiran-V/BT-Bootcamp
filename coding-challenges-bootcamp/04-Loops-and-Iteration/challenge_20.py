try:
    # Take user input
    n = int(input("Enter the value of N: "))
    
    # Validate input
    if n <= 0:
        print("Please enter a positive number.")
    else:
        # Display the series
        print(f"\nSeries up to {n}:")
        num = 1
        increment = 1
        
        while num <= n:
            print(num, end=" ")
            num += increment
            increment += 1
        print()  # New line after series

except ValueError:
    print("Invalid input. Please enter a valid integer.")