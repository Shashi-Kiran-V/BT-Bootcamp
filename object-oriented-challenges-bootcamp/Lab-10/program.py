# program.py
from employee_report import EmployeeReport
from role_builder import RoleBuilder
from roles import Roles
from employee import Employee

class Program:
    @staticmethod
    def main(args):
        employees = []

        print("Enter employee information")

        for i in range(4):  # creating 4 employees
            print(f"\nEmployee No : {i+1}")
            emp_id = input("Id : ")
            name = input("Name : ")
            basic = float(input("Basic : "))
            hra = float(input("HRA : "))
            allowance_percentage = float(input("Percentage of Allowance : "))

            print("Enter Role Id : ")
            print(f"{Roles.DEVELOPER}. {RoleBuilder.get_role_description(Roles.DEVELOPER)}")
            print(f"{Roles.TEST_ENGINEER}. {RoleBuilder.get_role_description(Roles.TEST_ENGINEER)}")
            print(f"{Roles.SR_DEVELOPER}. {RoleBuilder.get_role_description(Roles.SR_DEVELOPER)}")
            print(f"{Roles.DESIGNER}. {RoleBuilder.get_role_description(Roles.DESIGNER)}")
            role = int(input())

            # Create Employee object using parameterized constructor
            emp = Employee(emp_id, name, basic, hra, allowance_percentage, role)
            employees.append(emp)

        report_date = input("Enter the date of the report (dd/mm/yyyy) : ")
        report = EmployeeReport()
        report.report_date = report_date

        print("\n")
        report.display_employees(employees)

        input("Press Enter to exit...")


if __name__ == "__main__":
    import sys
    Program.main(sys.argv[1:])
