# 디펜스 게임
from heapq import *


def solution(n, k, enemy):
    answer = 0
    sum = 0
    heap = []
    for e in enemy:
        sum += e
        heappush(heap, -e)
        if n < sum:
            if k > 0:
                sum += heappop(heap)
                k -= 1
            else:
                break
        answer += 1

    return answer
