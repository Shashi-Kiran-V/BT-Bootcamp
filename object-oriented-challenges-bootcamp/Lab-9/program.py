# program.py
from employee_report import EmployeeReport
from role_builder import RoleBuilder
from roles import Roles
from employee import Employee

class Program:
    @staticmethod
    def main(args):
        employees = [None] * 4
        print("Enter employee information")

        for i in range(len(employees)):
            print(f"\nEmployee No : {i+1}")
            emp = Employee()
            emp.emp_id = input("Id : ")
            emp.name = input("Name : ")
            emp.basic = float(input("Basic : "))
            emp.hra = float(input("HRA : "))
            emp.allowance_percentage = float(input("Percentage of Allowance : "))

            print("Enter Role Id : ")
            print(f"{Roles.DEVELOPER}. {RoleBuilder.get_role_description(Roles.DEVELOPER)}")
            print(f"{Roles.TEST_ENGINEER}. {RoleBuilder.get_role_description(Roles.TEST_ENGINEER)}")
            print(f"{Roles.SR_DEVELOPER}. {RoleBuilder.get_role_description(Roles.SR_DEVELOPER)}")
            print(f"{Roles.DESIGNER}. {RoleBuilder.get_role_description(Roles.DESIGNER)}")
            emp.role = int(input())

            employees[i] = emp  # store employee in array

        report = EmployeeReport()
        report.report_date = input("Enter the date of the report (dd/mm/yyyy) : ")
        print("\n")
        report.display_employees(employees)

        input("Press Enter to exit...")


if __name__ == "__main__":
    import sys
    Program.main(sys.argv[1:])
