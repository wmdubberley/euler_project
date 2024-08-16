def sum_of_proper_divisors(n):
    """Returns the sum of proper divisors of n (divisors less than n)."""
    divisors_sum = 1  # 1 is a proper divisor of every number
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:  # Avoid adding the square root twice for perfect squares
                divisors_sum += n // i
    return divisors_sum

def find_amicable_numbers(limit):
    """Returns the sum of all amicable numbers under a given limit."""
    amicable_sum = 0
    for num in range(2, limit):
        # Find the sum of proper divisors of num
        div_sum = sum_of_proper_divisors(num)
        # Check if div_sum is a valid number and forms an amicable pair
        if div_sum != num and div_sum < limit:
            if sum_of_proper_divisors(div_sum) == num:
                amicable_sum += num
    return amicable_sum

# Example usage: find the sum of all amicable numbers under 10000
limit = 10000
result = find_amicable_numbers(limit)
print(f"The sum of all amicable numbers under {limit} is: {result}")
