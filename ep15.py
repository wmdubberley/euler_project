import math

def lattice_paths(n):
    # Calculate the binomial coefficient (2n choose n)
    return math.comb(2 * n, n)

# Example: Calculate the number of paths through a 20x20 grid
grid_size = 20
result = lattice_paths(grid_size)
print(f"The number of routes through a {grid_size}x{grid_size} grid is: {result}")