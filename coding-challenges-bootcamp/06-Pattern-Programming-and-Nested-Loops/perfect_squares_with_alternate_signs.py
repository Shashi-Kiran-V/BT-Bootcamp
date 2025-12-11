try:
    # Take user input
    n = int(input("Enter the number of rows: "))
    
    # Validate input
    if n <= 0:
        print("Please enter a positive number.")
    else:
        # Print perfect squares with alternating signs pattern
        print(f"\nPerfect squares with alternating signs pattern with {n} rows:")
        
        num = 1
        for i in range(1, n + 1):
            for j in range(i):
                square = num * num
                # Alternate signs based on num value
                if num % 2 == 0:
                    print(f"-{square}", end=" ")
                else:
                    print(square, end=" ")
                num += 1
            print()  # New line after each row

except ValueError:
    print("Invalid input. Please enter a valid integer.")