import math

def digit_factorial_sum(n):
    """Calculate the sum of the factorials of the digits of n."""
    return sum(math.factorial(int(digit)) for digit in str(n))

def find_curious_numbers():
    # Initialize the sum for curious numbers
    curious_sum = 0
    
    # We establish an upper bound to check up to 7-digit numbers
    upper_bound = 7 * math.factorial(9)
    
    # Iterate through possible numbers from 10 to the upper bound
    for num in range(10, upper_bound):
        if num == digit_factorial_sum(num):
            curious_sum += num
    
    return curious_sum

# Calculate the sum of all curious numbers
result = find_curious_numbers()
print(f"The sum of all curious numbers is: {result}")