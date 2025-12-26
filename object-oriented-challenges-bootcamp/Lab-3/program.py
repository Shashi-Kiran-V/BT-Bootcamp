from employee import Employee
from address import Address

class Program:
    @staticmethod
    def main(args):
        emp = Employee()
        Program.store_data(emp)
        Program.show_data(emp)

    @staticmethod
    def store_data(emp):
        emp.e_id="101"
        emp.e_name="shashi"
        emp.e_gender="Male"
        
        addr=Address()
        addr.address1="Hirehalli post Tumkur"
        addr.address2="Chikkabidarakallu Bengaluru"
        addr.city="Tumkur"
        addr.pincode="572104"

        emp.e_address=addr

    @staticmethod
    def show_data(emp):
        # ----------------Display the employee information
        print("Employee Id : ", emp.e_id)
        print("Employee Name : ", emp.e_name)
        print("Employee Gender : ", emp.e_gender)

        print("Employee Address : --------------")
        print("Address 1 : ", emp.e_address.address1)
        print("Address 2 : ", emp.e_address.address2)
        print("City : ", emp.e_address.city)
        print("PinCode : ", emp.e_address.pincode)
        print("----------------------------------")
        


if __name__ == "__main__":
    Program.main([])
