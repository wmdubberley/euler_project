def spiral_diagonal_sum(size):
    total_sum = 1  # Start with the center value (1)
    current_value = 1
    
    for n in range(3, size + 1, 2):
        step = n - 1
        
        for _ in range(4):
            current_value += step
            # print(current_value)
            total_sum += current_value
    
    return total_sum

# Example usage for a 1001x1001 spiral
size = 1001
result = spiral_diagonal_sum(size)
print(f"The sum of the numbers on the diagonals in a {size}x{size} spiral is: {result}")
