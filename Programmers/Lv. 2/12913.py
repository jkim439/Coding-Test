# 땅따먹기
def solution(land):
    cache = [land[0]]
    for r in range(1, len(land)):
        cache.append([])
        for c in range(4):
            prev = max(cache[-2][:c] + cache[-2][c + 1 :])
            cache[r].append(prev + land[r][c])
    return max(cache[-1])
