def collatz_sequence_length(n, cache):
    original_n = n
    length = 0
    
    while n != 1:
        if n in cache:
            length += cache[n]
            break
        
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        
        length += 1
    
    cache[original_n] = length
    return length

def find_longest_collatz_chain(limit):
    max_length = 0
    number_with_max_length = 0
    cache = {}

    for i in range(1, limit):
        length = collatz_sequence_length(i, cache)
        if length > max_length:
            max_length = length
            number_with_max_length = i
    
    return number_with_max_length

# Find the number under 1 million with the longest Collatz chain
result = find_longest_collatz_chain(1000000)
print(f"The starting number under one million that produces the longest chain is: {result}")
