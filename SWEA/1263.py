# 1263. [S/W 문제해결 응용] 8일차 - 사람 네트워크2
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

    answer = float("inf")
    for d in distances:
        answer = min(answer, sum(d))

    return answer


for t in range(1, int(input()) + 1):
    line = list(map(int, input().split()))
    n = line[0]
    graph1 = []
    graph2 = []

    for i in range(0, n * n, n):
        graph1.append(line[1:][i : i + n])

    for i in range(n):
        for j in range(n):
            if graph1[i][j] == 1:
                graph2.append([i, j, 1])

    print(f"#{t} {floyd_warshall(n, graph2)}")
