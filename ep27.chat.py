import math

def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def consecutive_primes(a, b):
    """Count the number of consecutive primes for quadratic expression n^2 + an + b."""
    n = 0
    while is_prime(n**2 + a*n + b):
        n += 1
    return n

def find_max_quadratic_prime():
    max_primes = 0
    product_ab = 0
    
    # Test all combinations of a and b
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            primes_count = consecutive_primes(a, b)
            if primes_count > max_primes:
                max_primes = primes_count
                product_ab = a * b
    
    return product_ab

# Find the product of coefficients a and b that produces the maximum number of primes
result = find_max_quadratic_prime()
print(f"The product of the coefficients a and b is: {result}")
