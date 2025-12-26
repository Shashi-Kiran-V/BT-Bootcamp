class DecimalSplitter:
    """
    Method to get the whole number from a double
    """
    @staticmethod
    def get_whole(number):
        return int(number)

    """
    Method to get the fractional part of a double number
    """
    @staticmethod
    def get_fraction(number):
        whole_part = int(number)
        fraction_part = number - whole_part
        return round(fraction_part, 2)

    """
    Method to check if a given number is odd or even
    """
    @staticmethod
    def is_odd(number):
        if number % 2 == 0:
            return "Even"
        else:
            return "Odd"
