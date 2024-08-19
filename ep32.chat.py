from itertools import permutations

def is_pandigital(multiplicand, multiplier, product):
    concatenated = str(multiplicand) + str(multiplier) + str(product)
    if len(concatenated) == 9 and set(concatenated) == set('123456789'):
        return True
    return False

def find_pandigital_products():
    products = set()
    
    # Try different combinations of multiplicand and multiplier
    # Case 1: multiplicand is 1 digit, multiplier is 4 digits
    for a in range(1, 10):  # 1-digit multiplicand
        for b in range(1234, 9877):  # 4-digit multiplier
            product = a * b
            if is_pandigital(a, b, product):
                products.add(product)
    
    # Case 2: multiplicand is 2 digits, multiplier is 3 digits
    for a in range(12, 99):  # 2-digit multiplicand
        for b in range(123, 988):  # 3-digit multiplier
            product = a * b
            if is_pandigital(a, b, product):
                products.add(product)
    
    # Return the sum of all unique products
    return sum(products)

# Calculate the sum of all products whose multiplicand/multiplier/product
# identity can be written as a 1 through 9 pandigital.
result = find_pandigital_products()
print(f"The sum of all pandigital products is: {result}")
