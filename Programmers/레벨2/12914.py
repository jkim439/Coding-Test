# 멀리 뛰기
def solution(n):
    if n < 3:
        return n
    cache = [1, 2]
    for i in range(2, n):
        cache.append(cache[i - 2] + cache[i - 1])
    return cache[-1] % 1234567
