try:
    # Take user input
    num = float(input("Enter a decimal number: "))
    
    # Separate whole and fractional parts
    whole_part = int(num)
    fractional_part = num - whole_part
    
    # Display results
    print(f"\nInput: {num}")
    print(f"Whole part: {whole_part}")
    print(f"Fractional part: {fractional_part:.10f}")

except ValueError:
    print("Invalid input. Please enter a valid decimal number.")