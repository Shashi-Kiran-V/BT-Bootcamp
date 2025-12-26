# employee_report.py
class EmployeeReport:
    def __init__(self, dt_report=""):
        self.report_date = dt_report

    def print_line(self):
        print("---------------------------------------------------------------------------")

    def display_header(self):
        self.print_line()
        print("EMPLOYEE REPORT\t\t\t\t")
        print("Date : " + self.report_date)
        self.print_line()

    def display_footer(self, count):
        self.print_line()
        print("Total Employees : " + str(count))
        self.print_line()

    def display_employees(self, employees):
        self.display_header()
        print("EMP_ID\tNAME\tROLE\t\tBASIC\tHRA\tALLOW\tSALARY")
        self.print_line()

        for emp in employees:
            role_desc = emp.get_role_description()
            allowance = emp.get_allowance()
            salary = emp.get_salary()
            print(f"{emp.emp_id}\t{emp.name}\t{role_desc}\t{emp.basic}\t{emp.hra}\t{allowance}\t{salary}")

        self.display_footer(len(employees))
