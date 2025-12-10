try:
    # Take user input
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest (per annum %): "))
    time = float(input("Enter the time period (in years): "))

    # Calculate simple interest
    simple_interest = (principal * rate * time) / 100

    # Calculate total amount
    total_amount = principal + simple_interest

    # Display results
    print("\n--- Simple Interest Calculation ---")
    print(f"Principal: Rs.{principal:.2f}")
    print(f"Rate of Interest: {rate}% per annum")
    print(f"Time Period: {time} years")
    print(f"Simple Interest: Rs.{simple_interest:.2f}")
    print(f"Total Amount: Rs.{total_amount:.2f}")

except ValueError:
    print("Invalid input. Please enter numeric values.")