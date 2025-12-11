try:
    # Take user input for array size
    n = int(input("Enter the size of the array: "))
    
    # Validate input
    if n <= 0:
        print("Please enter a positive number.")
    else:
        # Create an empty list to store elements
        arr = []
        
        # Take elements from user
        print(f"Enter {n} elements:")
        for i in range(n):
            element = int(input(f"Element {i + 1}: "))
            arr.append(element)
        
        # Calculate sum of all elements
        total_sum = sum(arr)
        
        # Display results
        print(f"\nArray: {arr}")
        print(f"Sum of all elements: {total_sum}")

except ValueError:
    print("Invalid input. Please enter valid integers.")