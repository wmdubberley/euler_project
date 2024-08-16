base = 2
exponent = 1000
print(pow(base,exponent))
digits = [int(digit) for digit in str(pow(base,exponent))]
print(digits)
print(sum(digits))