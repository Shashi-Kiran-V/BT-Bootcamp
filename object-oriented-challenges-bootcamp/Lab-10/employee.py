# employee.py
from salary_calculator import SalaryCalculator

class Employee:
    def __init__(self, emp_id="", name="", basic=0.0, hra=0.0, allowance_percentage=0.0, role=0):
        self.emp_id = emp_id
        self.name = name
        self.basic = basic
        self.hra = hra
        self.allowance_percentage = allowance_percentage
        self.role = role

    # Method to get allowance via SalaryCalculator
    def get_allowance(self):
        return SalaryCalculator.get_allowance(self)

    # Method to get salary via SalaryCalculator
    def get_salary(self):
        return SalaryCalculator.get_salary(self)
