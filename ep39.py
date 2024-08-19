def find_max_solutions(limit):
    max_solutions = 0
    best_p = 0
    
    for p in range(2, limit + 1):
        solutions = 0
        for a in range(1, p // 2):
            b = (p * (p - 2 * a)) // (2 * (p - a))
            c = p - a - b
            if a * a + b * b == c * c and a < b < c:
                solutions += 1
        if solutions > max_solutions:
            max_solutions = solutions
            best_p = p
    
    return best_p, max_solutions

# Find the value of p ≤ 1000 that maximizes the number of solutions
limit = 1000
result, num_solutions = find_max_solutions(limit)
print(f"The value of p that maximizes the number of solutions is: {result}, with {num_solutions} solutions.")
