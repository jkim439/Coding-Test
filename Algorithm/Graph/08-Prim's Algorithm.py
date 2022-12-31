from heapq import *


def prim(n, graph, start):
    adjacent = [[] for _ in range(n + 1)]
    for node1, node2, weight in graph:
        adjacent[node1].append([weight, node1, node2])
        adjacent[node2].append([weight, node2, node1])

    mst = []

    visited = {start}

    queue = adjacent[start]
    heapify(queue)

    while queue:
        weight, node1, node2 = heappop(queue)

        if node2 not in visited:
            visited.add(node2)
            mst.append([node1, node2, weight])

            for edge in adjacent[node2]:
                if edge[2] not in visited:
                    heappush(queue, edge)

    return mst


n = 7
graph = [
    [1, 2, 7],
    [1, 4, 5],
    [2, 1, 7],
    [2, 3, 8],
    [2, 4, 9],
    [2, 5, 7],
    [3, 2, 8],
    [3, 5, 5],
    [4, 1, 5],
    [4, 2, 9],
    [4, 5, 7],
    [4, 6, 6],
    [5, 2, 7],
    [5, 3, 5],
    [5, 4, 7],
    [5, 6, 8],
    [5, 7, 9],
    [6, 4, 6],
    [6, 5, 8],
    [6, 7, 11],
    [7, 5, 9],
    [7, 6, 11],
]

print(prim(n, graph, 1))
