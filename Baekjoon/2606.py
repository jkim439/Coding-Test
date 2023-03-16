# 바이러스
from collections import deque

c = int(input())
e = int(input())
adjacent = [[] for _ in range(c + 1)]
for _ in range(e):
    a, b = map(int, input().split())
    adjacent[a].append(b)
    adjacent[b].append(a)

visited = [0, 1]
queue = deque(adjacent[1])

while queue:
    node = queue.popleft()
    if node not in visited:
        visited.append(node)
        queue.extend(adjacent[node])

print(len(visited) - 2)
