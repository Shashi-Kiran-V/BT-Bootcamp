class AccountManager:
    """
    Method to store account details into the account object passed
    """
    def fill_account_data(self, acc):
        acc.acc_no = "004701"
        acc.name = "Nitesh"
        acc.balance = 45000.0

    """
    Method to display account details from the account object passed
    """
    def display_account_data(self, acc):
        print()
        print("AccNo : " + acc.acc_no)
        print("Name : " + acc.name)
        print("Balance : " + str(acc.balance))

        """
        The bug occurs because fill_account_data() is empty (pass), so account attributes are never initialized. This leads to a TypeError when attempting to concatenate a string with None.
        """