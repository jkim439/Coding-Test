# 1267. [S/W 문제해결 응용] 10일차 - 작업순서
from collections import deque

for t in range(1, 10):
    n, e = map(int, input().split())
    line = list(map(int, input().split()))
    graph = dict()

    for i in range(0, len(line) - 1, 2):
        if line[i + 1] not in graph:
            graph[line[i + 1]] = [line[i]]
        else:
            graph[line[i + 1]].append(line[i])

    visited = []
    queue = deque([i for i in range(1, n + 1)])
    while queue:
        edge = queue.popleft()
        if edge in graph:
            if any(i for i in graph[edge] if i in visited):
                visited.append(edge)
            else:
                queue.append(edge)
        else:
            visited.append(edge)

    answer = " ".join(list(map(str, visited)))

    print(f"#{t} {answer}")
