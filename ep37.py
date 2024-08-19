from util import is_prime


def truncatable(num):
    """Check if the prime is truncatable from left to right."""
    s = str(num)
    for i in range(1, len(s)):
        if not is_prime(int(s[i:])):
            return False
        for i in range(len(s) - 1, 0, -1):
            if not is_prime(int(s[:i])):
                return False
    return True

def find_truncatable_primes():
    truncatable_primes = []
    num = 11  # Start checking from 11 (since single-digit primes are excluded)
    
    while len(truncatable_primes) < 11:
        if is_prime(num):
            if truncatable(num):
                truncatable_primes.append(num)
        num += 1
    
    return truncatable_primes

# Find the truncatable primes and sum them
truncatable_primes = find_truncatable_primes()
result = sum(truncatable_primes)

print(f"The sum of the 11 truncatable primes is: {result}")
