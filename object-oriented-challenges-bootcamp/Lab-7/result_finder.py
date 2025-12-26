class ResultFinder:
    """
    Properties of the fields of this class
    """
    def __init__(self):
        self.marks1 = 0
        self.marks2 = 0
        self.marks3 = 0

    """
    Method to display marks obtained
    """

    @property
    def M1(self):
        return self.marks1
    
    @M1.setter
    def M1(self,value):
        self.marks1=value

    @property
    def M2(self):
        return self.marks2
    
    @M2.setter
    def M2(self,value):
        self.marks2=value

    @property
    def M3(self):
        return self.marks3
    
    @M3.setter
    def M3(self,value):
        self.marks3=value

    
    def display_marks(self):
        print("Marks 1 : " + str(self.marks1))
        print("Marks 2 : " + str(self.marks2))
        print("Marks 3 : " + str(self.marks3))

    """
    Method to get the total of the marks in subjects
    """
    def get_total(self):
        return self.marks1 + self.marks2 + self.marks3

    """
    Method to calculate the average of the marks
    """
    def get_average(self):
        return self.get_total() / 3

    """
    Method to get the result for the marks given
    """
    def get_result(self):
        average = self.get_average()
        if average >= 50:
            return "Pass"
        else:
            return "Fail"
