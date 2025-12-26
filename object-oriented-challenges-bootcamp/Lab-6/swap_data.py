class SwapData:
    """
    Properties of the class
    """
    def __init__(self):
        self._number1 = 0
        self._number2 = 0

    """
    Method to swap numbers of the class
    """
    @property
    def Number1(self):
        return self._number1
    
    @Number1.setter
    def Number1(self,value):
        self._number1=value

    @property
    def Number2(self):
        return self._number2
    
    @Number2.setter
    def Number2(self,value):
        self._number2=value

    def swap_values(self):
        temp = self.number1
        self.number1 = self.number2
        self.number2 = temp

    """
    Method to display the numbers before and after swapping
    """
    def display_values(self, str_msg):
        print(str_msg)
        print("Number 1 = " + str(self.number1))
        print("Number 2 = " + str(self.number2))
