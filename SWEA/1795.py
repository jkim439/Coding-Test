# 1795. 인수의 생일 파티
from heapq import *


def dijkstra(n, d, graph, start):
    adjacent = [[] for _ in range(n + 1)]
    for node1, node2, distance in graph:
        if d == 1:
            adjacent[node1].append([distance, node2])
        else:
            adjacent[node2].append([distance, node1])

    distances = [float("inf")] * (n + 1)
    distances[start] = 0
    distances[0] = 0

    queue = []
    heappush(queue, [0, start])

    while queue:
        cost, node = heappop(queue)

        for c, n in adjacent[node]:
            if cost + c < distances[n]:
                distances[n] = cost + c
                heappush(queue, [cost + c, n])

    return distances


for t in range(1, int(input()) + 1):
    n, m, x = map(int, input().split())
    graph = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph.append([a, b, c])

    answer = []
    for a, b in zip(dijkstra(n, 1, graph, x), dijkstra(n, 2, graph, x)):
        answer.append(a + b)

    print(f"#{t} {max(answer)}")
