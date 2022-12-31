def floyd_warshall(n, graph):
    distances = [[float("inf")] * n for _ in range(n)]
    for node1, node2, distance in graph:
        distances[node1][node2] = distance

    for k in range(n):
        distances[k][k] = 0
        for i in range(n):
            for j in range(n):
                distances[i][j] = min(
                    distances[i][j], distances[i][k] + distances[k][j]
                )
    return distances


n = 4
graph = [[0, 2, -2], [1, 0, 4], [1, 2, 3], [2, 3, 2], [3, 1, -1]]

print(floyd_warshall(n, graph))
