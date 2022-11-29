n, m, v = map(int, input().split())

g = [[] for _ in range(n + 1)]
for _ in range(m):
    n1, n2 = map(int, input().split())
    g[n1].append(n2)
    g[n2].append(n1)


def dfs(g, v):
    visited = []
    queue = [v]

    while queue:
        node = queue.pop()
        if node not in visited:
            visited.append(node)
            queue.extend(g[node])
    return visited


def bfs(g, v):
    for x in g:
        x.sort()
    visited = []
    queue = [v]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue.extend(g[node])
    return visited


print(n, m, v, g)
print(dfs(g, v))
print(bfs(g, v))
