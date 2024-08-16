def find_fibonacci_index_with_digits(digit_count):
    # Starting conditions for Fibonacci sequence
    a, b = 1, 1
    index = 2  # Since F(1) and F(2) are already initialized
    
    # Generate Fibonacci numbers until we find one with the required number of digits
    while True:
        a, b = b, a + b
        index += 1
        if len(str(b)) >= digit_count:
            return index

# Example usage: Find the index of the first Fibonacci number with 1000 digits
digit_count = 1000
index = find_fibonacci_index_with_digits(digit_count)
print(f"The index of the first Fibonacci number with {digit_count} digits is: {index}")