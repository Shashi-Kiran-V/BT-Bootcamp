class AccountManager1:
    """
    Method to fill account details into the account object passed
    """
    def fill_account_data(self, acc):
        acc._acc_no = "004701" # not invoking the setter method but directly accessing the attribute
        acc._name = "Nitesh" # not invoking the setter method but directly accessing the attribute
        acc._balance = 45000.0 # not invoking the setter method but directly accessing the attribute

    """
    Method to display account details from the account object passed
    """
    def display_account_data(self, acc):
        print("AccNo : " + acc._acc_no) # not invoking the getter method but directly accessing the attribute
        print("Name : " + acc._name) # not invoking the getter method but directly accessing the attribute
        print("Balance : " + str(acc._balance)) # not invoking the getter method but directly accessing the attribute
