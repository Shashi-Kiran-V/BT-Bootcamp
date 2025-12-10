
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))


    totalSum = num1 + num2 # calculating sum
    average = totalSum / 2 # calculating average

    # print the results
    print(f"\nFirst number: {num1}")
    print(f"Second number: {num2}")
    print(f"Sum: {totalSum}")
    print(f"Average: {average}")
    
except ValueError:
    print("Invalid input. Please enter numeric values.")