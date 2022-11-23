# 피보나치 수
def solution(n):
    cache = [0, 1]
    for i in range(2, n + 1):
        cache.append(cache[i - 2] + cache[i - 1])
    return cache[-1] % 1234567
