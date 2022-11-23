def dfs(n, i, graph, visited):
    visited[i] = 1
    for j in range(n):
        if graph[i][j] == 0 and visited[j] == 0:
            dfs(n, j, graph, visited)


n = 10
visited = [0 for _ in range(n)]
for i in range(n):
    if visited[i] == 0:
        dfs(n, i, [[]], visited)
