from fractions import Fraction

def is_curious_fraction(numerator, denominator):
    # Convert numbers to strings for digit manipulation
    str_num = str(numerator)
    str_den = str(denominator)
    
    # Check for common digits (not including 0)
    for digit in str_num:
        if digit in str_den and digit != '0':
            # Try to cancel the digit and form new fractions
            new_num_str = str_num.replace(digit, '', 1)
            new_den_str = str_den.replace(digit, '', 1)
            
            if new_num_str != '' and new_den_str != '':
                new_num = int(new_num_str)
                new_den = int(new_den_str)
                
                # Ensure new denominator is not zero
                if new_den != 0 and numerator * new_den == denominator * new_num:
                    return True
    return False

def find_curious_fractions():
    product = Fraction(1)  # Start with a fraction 1/1 to multiply
    for numerator in range(10, 100):
        for denominator in range(numerator + 1, 100):  # Ensure fraction is less than 1
            if is_curious_fraction(numerator, denominator):
                product *= Fraction(numerator, denominator)
    
    return product

# Find the product of all curious fractions in its lowest terms
curious_fraction_product = find_curious_fractions()

# Print the denominator of the product
print(f"The denominator of the product in its lowest terms is: {curious_fraction_product.denominator}")
