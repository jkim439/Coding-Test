def find_minimum_number_of_coins(n, coins):
    count = 0
    for coin in coins:
        count += n // coin
        n %= coin
    return count


print(find_minimum_number_of_coins(1260, [500, 100, 50, 10]))
