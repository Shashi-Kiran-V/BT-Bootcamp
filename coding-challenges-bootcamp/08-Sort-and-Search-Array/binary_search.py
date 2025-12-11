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
        print(f"Enter {n} elements (in sorted order):")
        for i in range(n):
            element = int(input(f"Element {i + 1}: "))
            arr.append(element)
        
        # Check if array is sorted in ascending order
        is_sorted = True
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                is_sorted = False
                break
        
        if not is_sorted:
            print("\nError: Array is not sorted in ascending order!")
            print(f"Array: {arr}")
        else:
            # Take search element from user
            search_element = int(input("\nEnter the element to search: "))
            
            # Binary search implementation
            left = 0
            right = n - 1
            found = False
            position = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if arr[mid] == search_element:
                    found = True
                    position = mid
                    break
                elif arr[mid] < search_element:
                    left = mid + 1
                else:
                    right = mid - 1
            
            # Display results
            print(f"\nArray: {arr}")
            if found:
                print(f"Element {search_element} found at position {position + 1}")
            else:
                print(f"Element {search_element} not found in the array")

except ValueError:
    print("Invalid input. Please enter valid integers.")