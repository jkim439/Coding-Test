# 배달
from heapq import *


def solution(N, road, K):
    distances = [float("inf")] * (N + 1)
    distances[1] = 0

    adjacent = [[] for _ in range(N + 1)]
    for r in road:
        adjacent[r[0]].append([r[2], r[1]])
        adjacent[r[1]].append([r[2], r[0]])

    queue = []
    heappush(queue, [0, 1])
    while queue:
        cost, node = heappop(queue)

        for c, n in adjacent[node]:
            if cost + c < distances[n]:
                distances[n] = cost + c
                heappush(queue, [cost + c, n])

    return len([item for item in distances if item <= K])
