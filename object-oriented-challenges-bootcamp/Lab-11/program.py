# program.py
from employee_report import EmployeeReport
from roles import Roles
from employee import Employee

class Program:
    @staticmethod
    def main(args):
        employees = [None] * 4

        print("Enter employee information")

        for i in range(4):
            print(f"\nEmployee No : {i+1}")
            emp = Employee()  # empty instance

            # Accept values from console
            emp.emp_id = input("Id : ")
            emp.name = input("Name : ")
            emp.basic = float(input("Basic : "))
            emp.hra = float(input("HRA : "))
            emp.allowance_percentage = float(input("Percentage of Allowance : "))

            print("Enter Role Id : ")
            print(f"{Roles.DEVELOPER}. DEVELOPER")
            print(f"{Roles.TEST_ENGINEER}. TEST_ENGINEER")
            print(f"{Roles.SR_DEVELOPER}. SR_DEVELOPER")
            print(f"{Roles.DESIGNER}. DESIGNER")
            role_input = int(input())
            emp.role = role_input

            employees[i] = emp

        dt_report = input("Enter the date of the report (dd/mm/yyyy) : ")
        report = EmployeeReport(dt_report)

        print("\n")
        report.display_employees(employees)

        input("Press Enter to exit...")


if __name__ == "__main__":
    import sys
    Program.main(sys.argv[1:])
