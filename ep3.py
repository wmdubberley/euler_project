def prime_factors(n):
    factors = []
    divisor = 2

    while divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor  # Divide n by divisor
        else:
            divisor += 1

    return factors

number = 600851475143
print("Prime factors of", number, "are:", prime_factors(number))