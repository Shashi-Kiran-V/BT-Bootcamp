# Coding Challenge 42: Generate Series - 1, -5, 9, -13, 17, -21, ... N terms

def generate_series(n):
    series = []
    for i in range(1, n + 1):
        term = ((-1) ** (i + 1)) * (4 * i - 3)
        series.append(term)
    return series

# ------- Run -------
try:
    n = int(input("Enter number of terms: "))
    print(generate_series(n))
except ValueError:
    print("Invalid input! Please enter an integer.")
