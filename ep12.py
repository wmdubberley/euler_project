import math

# Function to find the number of divisors of a number
def count_divisors(n):
    divisors_count = 0
    sqrt_n = int(math.sqrt(n))
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            divisors_count += 2  # i and n // i are both divisors
    if sqrt_n * sqrt_n == n:
        divisors_count -= 1  # Correct for a perfect square
    return divisors_count

# Find the first triangular number with more than 500 divisors
def find_triangle_number_with_divisors(limit):
    index = 1
    triangle_number = 0
    
    while True:
        # Generate the next triangular number
        triangle_number += index
        index += 1
        
        # Count the number of divisors
        divisors_count = count_divisors(triangle_number)
        
        # Check if the number of divisors exceeds the limit
        if divisors_count > limit:
            return triangle_number

# Find the first triangular number with more than 500 divisors
result = find_triangle_number_with_divisors(500)
print(f"The first triangular number with more than 500 divisors is: {result}")