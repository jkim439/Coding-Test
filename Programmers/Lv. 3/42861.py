# 섬 연결하기
from collections import defaultdict
from heapq import *


def solution(n, costs):
    answer = 0
    adjacent = defaultdict(list)
    for node1, node2, weight in costs:
        adjacent[node1].append([weight, node1, node2])
        adjacent[node2].append([weight, node2, node1])

    visited = {costs[0][0]}
    edges = adjacent[costs[0][0]]
    heapify(edges)

    while edges:
        weight, node1, node2 = heappop(edges)

        if node2 not in visited:
            visited.add(node2)
            answer += weight
            for edge in adjacent[node2]:
                if edge[2] not in visited:
                    heappush(edges, edge)

    return answer
