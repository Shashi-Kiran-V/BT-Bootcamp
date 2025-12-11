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
        
        # Take sorting preference from user
        print("\nChoose sorting order:")
        print("1. Ascending")
        print("2. Descending")
        choice = int(input("Enter your choice (1 or 2): "))
        
        # Sort array based on user choice
        if choice == 1:
            sorted_arr = sorted(arr)
            print(f"\nOriginal array: {arr}")
            print(f"Sorted array (Ascending): {sorted_arr}")
        elif choice == 2:
            sorted_arr = sorted(arr, reverse=True)
            print(f"\nOriginal array: {arr}")
            print(f"Sorted array (Descending): {sorted_arr}")
        else:
            print("Invalid choice. Please enter 1 or 2.")

except ValueError:
    print("Invalid input. Please enter valid integers.")