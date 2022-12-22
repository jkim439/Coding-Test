def bfs(n, graph, start):
    adjacent = [[] for _ in range(n + 1)]
    for node1, node2 in graph:
        adjacent[node1].append(node2)
        adjacent[node2].append(node1)

    for a in adjacent:
        a.sort(reverse=False)

    visited = []

    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue.extend(adjacent[node])

    return visited


n = 7
graph = [[5, 4], [5, 2], [1, 2], [3, 4], [3, 1]]

print(bfs(n, graph, 3))
