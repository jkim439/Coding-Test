# 등굣길
def solution(m, n, puddles):
    graph = [[0] * (m + 1) for i in range(n + 1)]

    for row in range(1, n + 1):
        for col in range(1, m + 1):
            if row == 1 and col == 1:
                graph[1][1] = 1
            elif [col, row] not in puddles:
                graph[row][col] = graph[row - 1][col] + graph[row][col - 1]

    return graph[n][m] % 1000000007
