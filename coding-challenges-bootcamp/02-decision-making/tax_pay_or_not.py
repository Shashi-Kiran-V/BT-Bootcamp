try:
    # Take user input
    name = input("Enter your name: ")
    
    # Validate that name contains only alphabetic characters and spaces
    if not name.replace(" ", "").isalpha():
        print("Invalid input. Name should contain only letters.")
    else:
        salary = float(input("Enter your salary: "))

        # Check if salary is greater than 3 lakhs (300000)
        if salary > 300000:
            print(f"\n{name}, your salary is Rs.{salary:.2f}")
            print("You must PAY TAX")
        else:
            print(f"\n{name}, your salary is Rs.{salary:.2f}")
            print("You are NOT required to pay tax")

except ValueError:
    print("Invalid input. Please enter valid values.")