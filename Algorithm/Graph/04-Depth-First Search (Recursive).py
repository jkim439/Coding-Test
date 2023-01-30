def dfs(i, n, graph, visited):
    visited[i] = 1
    for j in range(n):
        if visited[j] == 0 and graph[i][j] == 0:
            dfs(j, n, graph, visited)


n = 1
visited = [0] * n
for i in range(n):
    if visited[i] == 0:
        dfs(i, n, [[]], visited)
