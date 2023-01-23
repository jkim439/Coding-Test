# 가장 먼 노드
from heapq import *


def dijkstra(n, graph, start):
    adjacent = [[] for _ in range(n + 1)]
    for node1, node2, distance in graph:
        adjacent[node1].append([distance, node2])
        adjacent[node2].append([distance, node1])

    distances = [float("inf")] * (n + 1)
    distances[start] = 0

    queue = []
    heappush(queue, [0, start])

    while queue:
        cost, node = heappop(queue)

        for c, n in adjacent[node]:
            if cost + c < distances[n]:
                distances[n] = cost + c
                heappush(queue, [cost + c, n])

    return distances


def solution(n, edge):
    for e in edge:
        e.append(1)

    result = dijkstra(n, edge, 1)
    return result.count(max(result[1:]))
