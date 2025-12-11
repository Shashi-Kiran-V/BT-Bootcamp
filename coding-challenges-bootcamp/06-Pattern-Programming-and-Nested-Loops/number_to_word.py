try:
    # Take user input
    num = input("Enter a number: ")
    
    # Validate input - check if it contains only digits
    if not num.isdigit():
        print("Invalid input. Please enter a valid number.")
    else:
        # Dictionary to map digits to words
        digit_words = {
            '0': 'Zero',
            '1': 'One',
            '2': 'Two',
            '3': 'Three',
            '4': 'Four',
            '5': 'Five',
            '6': 'Six',
            '7': 'Seven',
            '8': 'Eight',
            '9': 'Nine'
        }
        
        # Convert each digit to word
        print(f"\nInput: {num}")
        print("Output: ", end="")
        
        for digit in num:
            print(digit_words[digit], end=" ")
        print()

except ValueError:
    print("Invalid input. Please enter a valid number.")