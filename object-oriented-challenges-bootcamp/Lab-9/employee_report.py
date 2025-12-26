from employee import Employee
from salary_calculator import SalaryCalculator
from role_builder import RoleBuilder
from roles import Roles

class EmployeeReport:
    """
    Property of the class
    """
    def __init__(self):
        self.report_date = ""

    """
    Method to print a line in a report
    """
    def print_line(self):
        print("---------------------------------------------------------------------------")

    """
    Method to display header information of the report
    """
    def display_header(self):
        self.print_line()
        print("EMPLOYEE REPORT\t\t\t\t")
        print("Date : " + self.report_date)
        self.print_line()

    """
    Method to display footer information in the report
    """
    def display_footer(self, count):
        self.print_line()
        print("Total Employees : " + str(count))
        self.print_line()

    """
    Method to display employees information
    """
    def display_employees(self, employees):
        self.display_header()

        print("EMP_ID\tNAME\tROLE\t\tBASIC\tHRA\tALLOW\tSALARY")
        self.print_line()

        # Placeholder for employee information printing
        # Original C# code does not include the loop for displaying details
        for emp in employees:
            role_desc = RoleBuilder.get_role_description(emp.role)
            allowance = SalaryCalculator.get_allowance(emp)
            salary = SalaryCalculator.get_salary(emp)
            print(f"{emp.emp_id}\t{emp.name}\t{role_desc}\t{emp.basic}\t{emp.hra}\t{allowance}\t{salary}")

        self.display_footer(len(employees))
