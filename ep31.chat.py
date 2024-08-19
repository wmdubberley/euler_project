def count_ways_to_make_change(target, coins):
    # Initialize a list with (target + 1) elements, all set to 0
    ways = [0] * (target + 1)
    
    # There is one way to make 0p (using no coins)
    ways[0] = 1
    
    # For each coin, update the ways to make change
    for coin in coins:
        for amount in range(coin, target + 1):
            ways[amount] += ways[amount - coin]
    
    return ways[target]

# Define the target and the coins
target = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]

# Calculate the number of ways to make £2
result = count_ways_to_make_change(target, coins)
print(f"The number of ways to make £2 using any number of coins is: {result}")
