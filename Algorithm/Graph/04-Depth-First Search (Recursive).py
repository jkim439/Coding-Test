def dfs(i, n, graph, visited):
    visited[i] = 1
    for j in range(n):
        if graph[i][j] != 0 and visited[j] == 0:
            dfs(j, n, graph, visited)


answer = 0
n = 3
graph = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
visited = [0] * n

for i in range(n):
    if visited[i] == 0:
        dfs(i, n, graph, visited)
        answer += 1

print(answer)
