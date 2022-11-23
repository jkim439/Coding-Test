def fibonacci_dynamic_programming(n):
    cache = [0, 1]
    for i in range(2, n + 1):
        cache.append(cache[i - 2] + cache[i - 1])
    return cache[-1]


print(fibonacci_dynamic_programming(10))
