def bfs(m, n, graph):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    visited = [[0] * (n + 1) for _ in range(m + 1)]
    visited[0][0] = 1

    queue = [[0, 0]]

    while queue:
        y, x = queue.pop(0)

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if (
                0 <= ny <= m
                and 0 <= nx <= n
                and visited[ny][nx] == 0
                and graph[ny][nx] == 1
            ):
                visited[ny][nx] = visited[y][x] + 1
                queue.append([ny, nx])

    return visited[m][n]


print(
    bfs(
        3,
        5,
        [
            [1, 0, 1, 1, 1, 1],
            [1, 0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1, 1],
            [1, 1, 1, 0, 1, 1],
        ],
    )
)
