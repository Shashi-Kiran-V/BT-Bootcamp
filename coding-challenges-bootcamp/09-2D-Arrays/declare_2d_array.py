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
        
        # Display 2D array row-wise
        print("\n2D Array:")
        for i in range(rows):
            for j in range(cols):
                print(arr_2d[i][j], end=" ")
            print()  # New line after each row

except ValueError:
    print("Invalid input. Please enter valid integers.")