try:
    # Take user input
    num = input("Enter a number: ")
    
    # Handle negative numbers
    is_negative = num.startswith('-')
    if is_negative:
        num = num[1:]  # Remove the minus sign
    
    # Reverse the string
    reversed_num = num[::-1]
    
    # Apply negative sign if original was negative
    if is_negative:
        reversed_num = '-' + reversed_num
    
    # Display results
    print(f"\nOriginal number: {num if not is_negative else '-' + num}")
    print(f"Reversed number: {reversed_num}")

except ValueError:
    print("Invalid input. Please enter a valid number.")