for a in range(1, 10000):
    for b in range(a + 1, 10000):
        c = 10000 - a - b
        if a**2 + b**2 == c**2:
            print(f"Pythagorean triplet: a={a}, b={b}, c={c}")
            print(f"Product abc = {a * b * c}")
            break