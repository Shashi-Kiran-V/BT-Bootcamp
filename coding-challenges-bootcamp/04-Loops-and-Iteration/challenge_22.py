# Generate the series: 1, 4, 7, 12, 23, ...

def generate_series(n):
    if n <= 0:
        return []
    series = [1]
    if n == 1:
        return series
    series.append(4)
    if n == 2:
        return series
    
    for i in range(2, n):
        # current term = previous term + difference
        # difference = previous term - series[i-2] + series[i-1] - series[i-2]
        # Using known pattern: next_term = prev + prev_diff + prev_prev_diff
        next_term = series[i-1] + (series[i-1] - series[i-2]) + (series[i-2] - series[i-3] if i-3 >= 0 else 0)
        series.append(next_term)
    return series

# Example: first 10 terms
n = 10
print(generate_series(n))

try:
    # Take user input
    n = int(input("Enter the value of N: "))
    
    # Validate input
    if n <= 0:
        print("Please enter a positive number.")
    else:
        # Display the series
        print(f"\nSeries up to {n}:")
        num = 1
        increment = 3
        
        while num <= n:
            print(num, end=" ")
            num += increment
            increment += increment
        print()  # New line after series

except ValueError:
    print("Invalid input. Please enter a valid integer.")
