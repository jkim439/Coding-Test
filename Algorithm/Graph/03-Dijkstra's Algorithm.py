from heapq import *


def dijkstra(graph, n):
    n += 1
    distances = [float("inf")] * n
    distances[1] = 0

    adjacent = [[] for _ in range(n)]
    for g in graph:
        adjacent[g[0]].append([g[2], g[1]])
        adjacent[g[1]].append([g[2], g[0]])

    queue = []
    heappush(queue, [0, 1])
    while queue:
        cost, node = heappop(queue)

        for c, n in adjacent[node]:
            if cost + c < distances[n]:
                distances[n] = cost + c
                heappush(queue, [cost + c, n])

    return distances


graph = [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]]
n = 5
print(dijkstra(graph, n))
