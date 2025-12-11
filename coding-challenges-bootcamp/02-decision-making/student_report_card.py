try:
    # Take student name and scores as input
    name = input("Enter student's name: ")
    
    # Validate name
    if not name.replace(" ", "").isalpha():
        print("Invalid input. Name should contain only letters.")
    else:
        # Take scores for three subjects
        score1 = float(input("Enter score for Subject 1: "))
        score2 = float(input("Enter score for Subject 2: "))
        score3 = float(input("Enter score for Subject 3: "))
        
        # Calculate total and average
        total = score1 + score2 + score3
        average = total / 3
        
        # Determine class based on average
        if average >= 60:
            class_secured = "1st Class"
        elif average >= 50:
            class_secured = "2nd Class"
        elif average >= 35:
            class_secured = "Pass Class"
        else:
            class_secured = "Fail"
        
        # Display report card
        print("\n--- STUDENT REPORT CARD ---")
        print(f"Name: {name}")
        print(f"Subject 1: {score1}")
        print(f"Subject 2: {score2}")
        print(f"Subject 3: {score3}")
        print(f"Total: {total}")
        print(f"Average: {average:.2f}")
        print(f"Class: {class_secured}")

except ValueError:
    print("Invalid input. Please enter valid numeric values for scores.")