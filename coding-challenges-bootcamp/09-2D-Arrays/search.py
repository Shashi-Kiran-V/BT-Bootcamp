try:
    # Take user input for number of rows and columns
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    
    # Validate input
    if rows <= 0 or cols <= 0:
        print("Please enter positive numbers for rows and columns.")
    else:
        # Create a 2D array (list of lists)
        arr_2d = []
        
        # Take elements from user
        print(f"\nEnter {rows * cols} elements:")
        for i in range(rows):
            row = []
            for j in range(cols):
                element = int(input(f"Element [{i}][{j}]: "))
                row.append(element)
            arr_2d.append(row)
        
        # Take search element from user
        search_element = int(input("\nEnter the element to search: "))
        
        # Search for the element in 2D array
        found = False
        position_row = -1
        position_col = -1
        
        for i in range(rows):
            for j in range(cols):
                if arr_2d[i][j] == search_element:
                    found = True
                    position_row = i
                    position_col = j
                    break
            if found:
                break
        
        # Display 2D array and search result
        print("\n2D Array:")
        for i in range(rows):
            for j in range(cols):
                print(arr_2d[i][j], end=" ")
            print()
        
        if found:
            print(f"\nElement {search_element} found at position [{position_row}][{position_col}]")
        else:
            print(f"\nElement {search_element} not found in the array")

except ValueError:
    print("Invalid input. Please enter valid integers.")