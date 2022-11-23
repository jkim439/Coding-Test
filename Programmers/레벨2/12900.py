# 2 x n 타일링
def solution(n):
    cache = [1, 2]
    for i in range(2, n):
        cache.append(cache[i - 2] + cache[i - 1])
    return cache[-1]
