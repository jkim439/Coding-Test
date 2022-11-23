from collections import defaultdict
from heapq import *


def prim(graph, start):
    mst = []

    adjacent = defaultdict(list)
    for node1, node2, weight in graph:
        adjacent[node1].append([weight, node1, node2])
        adjacent[node2].append([weight, node2, node1])

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


graph = [
    ["A", "B", 7],
    ["A", "D", 5],
    ["B", "A", 7],
    ["B", "C", 8],
    ["B", "D", 9],
    ["B", "E", 7],
    ["C", "B", 8],
    ["C", "E", 5],
    ["D", "A", 5],
    ["D", "B", 9],
    ["D", "E", 7],
    ["D", "F", 6],
    ["E", "B", 7],
    ["E", "C", 5],
    ["E", "D", 7],
    ["E", "F", 8],
    ["E", "G", 9],
    ["F", "D", 6],
    ["F", "E", 8],
    ["F", "G", 11],
    ["G", "E", 9],
    ["G", "F", 11],
]

print(prim(graph, "A"))
