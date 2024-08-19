import math
from util import sieve_of_eratosthenes

def rotate_number(num):
    """Generate all rotations of a number's digits."""
    s = str(num)
    return [int(s[i:] + s[:i]) for i in range(len(s))]

def is_circular_prime(num, prime_set):
    """Check if all rotations of a number are prime."""
    rotations = rotate_number(num)
    return all(rotation in prime_set for rotation in rotations)

def count_circular_primes(limit):
    primes = sieve_of_eratosthenes(limit)
    prime_set = set(primes)
    circular_prime_count = 0
    
    for prime in primes:
        if is_circular_prime(prime, prime_set):
            circular_prime_count += 1
    
    return circular_prime_count

# Count circular primes below one million
result = count_circular_primes(1000000)
print(f"The number of circular primes below one million is: {result}")