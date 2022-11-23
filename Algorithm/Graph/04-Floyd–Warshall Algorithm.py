def floyd_warshall(graph):
    n = len(graph) - 1
    distances = [[float("inf")] * n for _ in range(n)]

    for i, j, edge in graph:
        distances[i][j] = edge

    for k in range(n):
        distances[k][k] = 0
        for i in range(n):
            for j in range(n):
                distances[i][j] = min(
                    distances[i][j], distances[i][k] + distances[k][j]
                )
    return distances


data = [[0, 2, -2], [1, 0, 4], [1, 2, 3], [2, 3, 2], [3, 1, -1]]

print(floyd_warshall(data))
