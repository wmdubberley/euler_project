def sum_of_proper_divisors(n):
    """Calculate the sum of proper divisors of n."""
    divisors_sum = 1  # 1 is always a proper divisor
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    return divisors_sum

def find_abundant_numbers(limit):
    """Find all abundant numbers up to a given limit."""
    abundant_numbers = []
    for i in range(12, limit + 1):
        if sum_of_proper_divisors(i) > i:
            abundant_numbers.append(i)
    return abundant_numbers

def find_non_abundant_sums(limit):
    """Find the sum of all positive integers that cannot be written as the sum of two abundant numbers."""
    abundant_numbers = find_abundant_numbers(limit)
    abundant_sums = [False] * (limit + 1)
    
    # Mark all sums of two abundant numbers
    for i in range(len(abundant_numbers)):
        for j in range(i, len(abundant_numbers)):
            abundant_sum = abundant_numbers[i] + abundant_numbers[j]
            if abundant_sum <= limit:
                abundant_sums[abundant_sum] = True
            else:
                break
    
    # Sum all numbers that are not the sum of two abundant numbers
    non_abundant_sum = sum(i for i in range(1, limit + 1) if not abundant_sums[i])
    
    return non_abundant_sum

# Set the limit as 28123
limit = 28123
result = find_non_abundant_sums(limit)
print(f"The sum of all positive integers which cannot be written as the sum of two abundant numbers is: {result}")
