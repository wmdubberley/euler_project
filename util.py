from typing import Generator
import math


def fibonacci_generator() -> Generator[int,None,None]:
    a,b=0,1
    while True:
        yield a
        a,b = b, (a+b)
        
def decimal_to_binary(n):
    binary = ''
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary

def sieve_of_eratosthenes(limit):
    """Generate a list of prime numbers up to the given limit using the Sieve of Eratosthenes."""
    sieve = [True] * limit
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    for start in range(2, int(math.sqrt(limit)) + 1):
        if sieve[start]:
            for i in range(start * start, limit, start):
                sieve[i] = False
    return [num for num, is_prime in enumerate(sieve) if is_prime]

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def get_square(n):
    return n*n

def is_pandigital(num):
    """Check if a number is 1 to 9 pandigital."""
    num_str = str(num)
    return len(num_str) == 9 and set(num_str) == set('123456789')
