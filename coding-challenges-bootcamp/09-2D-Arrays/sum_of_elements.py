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
        
        # Calculate sum of all elements
        total_sum = 0
        for i in range(rows):
            for j in range(cols):
                total_sum += arr_2d[i][j]
        
        # Display 2D array and sum
        print("\n2D Array:")
        for i in range(rows):
            for j in range(cols):
                print(arr_2d[i][j], end=" ")
            print()
        
        print(f"\nSum of all elements: {total_sum}")

except ValueError:
    print("Invalid input. Please enter valid integers.")