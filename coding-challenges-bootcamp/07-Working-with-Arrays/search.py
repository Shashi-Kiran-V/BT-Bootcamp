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
        
        # Take search element from user
        search_element = int(input("\nEnter the element to search: "))
        
        # Search for the element
        found = False
        position = -1
        
        for i in range(n):
            if arr[i] == search_element:
                found = True
                position = i
                break
        
        # Display results
        print(f"\nArray: {arr}")
        if found:
            print(f"Element {search_element} found at position {position + 1}")
        else:
            print(f"Element {search_element} not found in the array")

except ValueError:
    print("Invalid input. Please enter valid integers.")