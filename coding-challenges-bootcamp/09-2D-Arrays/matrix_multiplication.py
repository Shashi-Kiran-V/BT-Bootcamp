try:
    # Input dimensions for Matrix A
    r1 = int(input("Enter rows for Matrix A: "))
    c1 = int(input("Enter columns for Matrix A: "))

    # Input dimensions for Matrix B
    r2 = int(input("Enter rows for Matrix B: "))
    c2 = int(input("Enter columns for Matrix B: "))

    # Matrix multiplication rule check
    if c1 != r2:
        print("\nMatrix multiplication NOT possible!")
        print("Columns of A must be equal to rows of B.")
    else:
        # Input Matrix A
        print("\nEnter elements for Matrix A:")
        A = []
        for i in range(r1):
            row = []
            for j in range(c1):
                row.append(int(input(f"A[{i}][{j}]: ")))
            A.append(row)

        # Input Matrix B
        print("\nEnter elements for Matrix B:")
        B = []
        for i in range(r2):
            row = []
            for j in range(c2):
                row.append(int(input(f"B[{i}][{j}]: ")))
            B.append(row)

        # Initialize Result Matrix
        result = [[0 for _ in range(c2)] for _ in range(r1)]

        # Matrix multiplication logic
        for i in range(r1):
            for j in range(c2):
                for k in range(c1):
                    result[i][j] += A[i][k] * B[k][j]

        # Display Result
        print("\nResultant Matrix (A × B):")
        for row in result:
            for val in row:
                print(val, end=" ")
            print()

except ValueError:
    print("Invalid input! Please enter integers only.")
