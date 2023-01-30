def fibonacci_dynamic_programming(n):
    cache = [0, 1]
    for _ in range(2, n + 1):
        cache.append(cache[-2] + cache[-1])
    return cache[-1]


print(fibonacci_dynamic_programming(10))
