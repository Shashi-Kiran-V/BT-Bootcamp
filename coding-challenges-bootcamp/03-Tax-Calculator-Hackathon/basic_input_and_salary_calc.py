# Complete Employee Salary, Tax, Net Salary, and Report System
# Challenges 11-16 Integrated with Input Validation Rules

import re

def validate_name(name):
    if not name or not name.replace(" ", "").isalpha() or len(name) > 50:
        raise ValueError("Name must be non-empty, alphabets only, max 50 characters.")
    return name

def validate_emp_id(emp_id):
    if not (5 <= len(emp_id) <= 10) or not emp_id.isalnum():
        raise ValueError("EmpID must be alphanumeric and 5-10 characters long.")
    return emp_id

def validate_basic_salary(value):
    num = float(value)
    if num <= 0 or num > 100000000:
        raise ValueError("Basic Salary must be positive and ≤ ₹1,00,00,000.")
    return num

def validate_special_allowances(value):
    num = float(value)
    if num < 0 or num > 100000000:
        raise ValueError("Special Allowances must be non-negative and ≤ ₹1,00,00,000.")
    return num

def validate_bonus_percentage(value):
    num = float(value)
    if num < 0 or num > 100:
        raise ValueError("Bonus Percentage must be between 0 and 100.")
    return num

def calculate_gross_salary(basic_salary, special_allowances, bonus_percentage):
    gross_monthly = basic_salary + special_allowances
    if gross_monthly <= 0:
        raise ValueError("Gross Monthly Salary must be greater than zero.")
    annual_gross = gross_monthly * 12
    if annual_gross > 1000000000:
        raise ValueError("Annual Gross Salary exceeds realistic value.")
    bonus_amount = (bonus_percentage / 100) * annual_gross
    annual_gross += bonus_amount
    return gross_monthly, annual_gross

def calculate_taxable_income(annual_gross_salary):
    standard_deduction = 50000
    taxable_income = annual_gross_salary - standard_deduction
    if taxable_income < 0:
        taxable_income = 0
    return standard_deduction, taxable_income

def calculate_tax(taxable_income):
    tax = 0
    ti = taxable_income

    if taxable_income > 1500000:
        tax += (taxable_income - 1500000) * 0.30
        taxable_income = 1500000
    if taxable_income > 1200000:
        tax += (taxable_income - 1200000) * 0.20
        taxable_income = 1200000
    if taxable_income > 900000:
        tax += (taxable_income - 900000) * 0.15
        taxable_income = 900000
    if taxable_income > 600000:
        tax += (taxable_income - 600000) * 0.10
        taxable_income = 600000
    if taxable_income > 300000:
        tax += (taxable_income - 300000) * 0.05

    if ti <= 700000:
        tax = 0

    cess = tax * 0.04
    total_tax = tax + cess
    return tax, cess, total_tax

def calculate_net_salary(annual_gross_salary, total_tax):
    return annual_gross_salary - total_tax

def generate_report(name, emp_id, gross_monthly_salary, annual_gross_salary,
                    standard_deduction, taxable_income, tax_before_cess, cess, total_tax, net_salary):
    print("\n" + "-"*60)
    print("{:^60}".format("Employee Tax Report"))
    print("-"*60)
    print(f"{'Field':35} | {'Details'}")
    print("-"*60)
    print(f"{'Name':35} | {name}")
    print(f"{'Employee ID':35} | {emp_id}")
    print(f"{'Gross Monthly Salary':35} | ₹{gross_monthly_salary:,.2f}")
    print(f"{'Annual Gross Salary':35} | ₹{annual_gross_salary:,.2f}")
    print(f"{'Standard Deduction':35} | ₹{standard_deduction:,.2f}")
    print(f"{'Taxable Income':35} | ₹{taxable_income:,.2f}")
    print(f"{'Tax Before Cess':35} | ₹{tax_before_cess:,.2f}")
    print(f"{'4% Health & Education Cess':35} | ₹{cess:,.2f}")
    print(f"{'Total Tax Payable':35} | ₹{total_tax:,.2f}")
    print(f"{'Annual Net Salary':35} | ₹{net_salary:,.2f}")
    print("-"*60)

# ---------------- MAIN PROGRAM ----------------
try:
    # Employee Inputs with Validation
    while True:
        try:
            name = validate_name(input("Enter Employee Name: "))
            break
        except ValueError as e:
            print("Error:", e)

    while True:
        try:
            emp_id = validate_emp_id(input("Enter Employee ID: "))
            break
        except ValueError as e:
            print("Error:", e)

    while True:
        try:
            basic_salary = validate_basic_salary(input("Enter Basic Monthly Salary: "))
            break
        except ValueError as e:
            print("Error:", e)

    while True:
        try:
            special_allowances = validate_special_allowances(input("Enter Special Allowances (Monthly): "))
            break
        except ValueError as e:
            print("Error:", e)

    while True:
        try:
            bonus_percentage = validate_bonus_percentage(input("Enter Bonus Percentage (% of Annual Gross Salary): "))
            break
        except ValueError as e:
            print("Error:", e)

    # Calculations
    gross_monthly_salary, annual_gross_salary = calculate_gross_salary(
        basic_salary, special_allowances, bonus_percentage
    )

    standard_deduction, taxable_income = calculate_taxable_income(annual_gross_salary)
    tax_before_cess, cess, total_tax = calculate_tax(taxable_income)
    net_salary = calculate_net_salary(annual_gross_salary, total_tax)

    # Generate Tabular Report
    generate_report(name, emp_id, gross_monthly_salary, annual_gross_salary,
                    standard_deduction, taxable_income, tax_before_cess, cess, total_tax, net_salary)

except Exception as e:
    print("Something went wrong! Please check your inputs again.\nError:", e)
