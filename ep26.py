def find_recurring_cycle_length(d):
    # Remainders will be stored in a dictionary with their positions
    remainders = {}
    remainder = 1
    position = 0
    
    while remainder != 0:
        # If the remainder repeats, we found the recurring cycle
        if remainder in remainders:
            return position - remainders[remainder]
        
        # Store the position of the current remainder
        remainders[remainder] = position
        
        # Long division step: Multiply remainder by 10 and take mod d
        remainder = (remainder * 10) % d
        position += 1
    
    # If remainder becomes zero, there's no recurring cycle
    return 0

def find_longest_recurring_cycle(limit):
    max_length = 0
    max_d = 0
    
    for d in range(2, limit):
        cycle_length = find_recurring_cycle_length(d)
        if cycle_length > max_length:
            max_length = cycle_length
            max_d = d
    
    return max_d, max_length

# Find the denominator with the longest recurring cycle for 1/d where d < 1000
limit = 1000
denominator, length = find_longest_recurring_cycle(limit)
print(f"The denominator with the longest recurring cycle under {limit} is: {denominator} with a cycle length of {length}")
