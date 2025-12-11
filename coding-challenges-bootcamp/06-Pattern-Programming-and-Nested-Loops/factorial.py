try:
    # Take user input
    n = int(input("Enter the number of rows: "))
    
    # Validate input
    if n <= 0:
        print("Please enter a positive number.")
    else:
        # Print factorial pattern
        print(f"\nFactorial pattern with {n} rows:")
        
        num = 1
        for i in range(1, n + 1):
            for j in range(i):
                factorial = 1
                for k in range(1, num + 1):
                    factorial *= k
                print(factorial, end=" ")
                num += 1
            print()  # New line after each row

except ValueError:
    print("Invalid input. Please enter a valid integer.")