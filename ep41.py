import itertools
from util import is_prime


def find_largest_pandigital_prime():
    # We will check 7-digit pandigital numbers and smaller since 8 and 9-digit
    # pandigital numbers cannot be prime.
    for n in range(7, 0, -1):
        pandigitals = itertools.permutations('1234567'[:n])
        # Check pandigital numbers in descending order to find the largest prime
        for p in sorted(pandigitals, reverse=True):
            num = int(''.join(p))
            if is_prime(num):
                return num

# Find the largest pandigital prime
largest_pandigital_prime = find_largest_pandigital_prime()
print(f"The largest pandigital prime is: {largest_pandigital_prime}")