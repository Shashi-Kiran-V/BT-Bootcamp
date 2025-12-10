try:
    # Take user input
    total_amount = float(input("Enter the total amount: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate discount amount
    discount_amount = (total_amount * discount_percent) / 100

    # Calculate final amount after discount
    final_amount = total_amount - discount_amount

    # Display results
    print("\n--- Discount Calculation ---")
    print(f"Total Amount: Rs.{total_amount:.2f}")
    print(f"Discount Percentage: {discount_percent}%")
    print(f"Discount Amount: Rs.{discount_amount:.2f}")
    print(f"Final Amount: Rs.{final_amount:.2f}")

except ValueError:
    print("Invalid input. Please enter numeric values.")