import math

def get_lexicographic_permutation(digits, n):
    # Create a list of available digits
    available_digits = digits[:]
    
    # The result permutation
    result = []
    
    # Adjust n for zero-indexing
    n -= 1
    
    # Loop until we have built the permutation
    while available_digits:
        # Determine the block size for the current set of permutations
        block_size = math.factorial(len(available_digits) - 1)
        
        # Determine which digit to take next
        index = n // block_size
        result.append(available_digits.pop(index))
        
        # Update n to the correct index within the current block
        n %= block_size
    
    # Join the list into a string and return it
    return ''.join(map(str, result))

# Example usage to find the millionth permutation
digits = list(range(10))  # The digits 0 to 9
millionth_permutation = get_lexicographic_permutation(digits, 1000000)
print(f"The millionth lexicographic permutation is: {millionth_permutation}")
