def sum_of_primes(limit):
    # Create a boolean array to mark primes, all initialized to True
    sieve = [True] * limit
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers

    for start in range(2, int(limit ** 0.5) + 1):
        if sieve[start]:
            # Mark multiples of the current prime as False
            for multiple in range(start*start, limit, start):
                sieve[multiple] = False

    # Sum all the indices that are marked True (which are prime numbers)
    return sum(i for i, is_prime in enumerate(sieve) if is_prime)

# Define the limit
limit = 2_000_000

# Calculate and print the sum of primes below the limit
result = sum_of_primes(limit)
print(result)
