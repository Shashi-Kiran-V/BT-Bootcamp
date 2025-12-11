# Simple version with try–except for invalid inputs

try:
    name = input("Enter Employee Name: ")
    if not name.replace(" ", "").isalpha():
        raise ValueError("Name must contain only letters.")

    emp_id = input("Enter Employee ID: ")

    basic_salary = float(input("Enter Basic Monthly Salary: "))
    special_allowances = float(input("Enter Special Allowances (Monthly): "))
    bonus_percentage = float(input("Enter Bonus Percentage (% of Annual Gross Salary): "))

    if basic_salary < 0 or special_allowances < 0 or bonus_percentage < 0:
        raise ValueError("Salary values cannot be negative.")

    gross_monthly_salary = basic_salary + special_allowances
    annual_gross_salary = gross_monthly_salary * 12
    bonus_amount = (bonus_percentage / 100) * annual_gross_salary
    annual_gross_salary += bonus_amount

    print("\n----- Employee Salary Details -----")
    print("Name:", name)
    print("Employee ID:", emp_id)
    print("Gross Monthly Salary: ₹", gross_monthly_salary)
    print("Annual Gross Salary (including bonus): ₹", annual_gross_salary)

except ValueError as e:
    print("Error:", e)

except Exception:
    print("Something went wrong! Please check your inputs again.")
