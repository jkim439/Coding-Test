# 야근 지수
from heapq import *


def solution(n, works):
    works = [-i for i in works]
    heapify(works)

    t = 0
    while t < n:
        pop = heappop(works)
        if pop == 0:
            return 0
        else:
            heappush(works, pop + 1)
            t += 1

    return sum([i**2 for i in works])
