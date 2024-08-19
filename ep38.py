from util import is_pandigital

def find_largest_pandigital():
    largest_pandigital = 0
    
    # Iterate over possible values of n
    for n in range(1, 10000):  # The limit is based on ensuring the concatenated product doesn't exceed 9 digits
        concatenated_product = ""
        i = 1
        
        # Generate concatenated product by multiplying n by (1, 2, 3, ...)
        while len(concatenated_product) < 9:
            concatenated_product += str(n * i)
            i += 1
        
        # Check if concatenated product is exactly 9 digits and is pandigital
        if len(concatenated_product) == 9 and is_pandigital(concatenated_product):
            largest_pandigital = max(largest_pandigital, int(concatenated_product))
    
    return largest_pandigital

# Find the largest pandigital number
result = find_largest_pandigital()
print(f"The largest 1 to 9 pandigital number is: {result}")