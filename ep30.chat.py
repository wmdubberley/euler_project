def sum_of_fifth_powers():
    # Define the upper bound as discussed
    upper_bound = 6 * (9 ** 5)
    
    # Initialize the result
    total_sum = 0
    
    # Iterate through the range
    for num in range(2, upper_bound + 1):
        # Calculate the sum of the fifth powers of the digits
        digit_power_sum = sum(int(digit) ** 5 for digit in str(num))
        
        # Check if the number equals the sum of the fifth powers of its digits
        if num == digit_power_sum:
            total_sum += num
    
    return total_sum

# Find the sum of all numbers that can be written as the sum of fifth powers of their digits
result = sum_of_fifth_powers()
print(f"The sum of all the numbers that can be written as the sum of fifth powers of their digits is: {result}")
