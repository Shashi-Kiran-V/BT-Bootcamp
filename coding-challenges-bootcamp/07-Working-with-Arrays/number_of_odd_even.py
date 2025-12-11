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
        
        # Count odd and even numbers
        even_count = 0
        odd_count = 0
        
        for element in arr:
            if element % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        
        # Display results
        print(f"\nArray: {arr}")
        print(f"Number of even elements: {even_count}")
        print(f"Number of odd elements: {odd_count}")

except ValueError:
    print("Invalid input. Please enter valid integers.")