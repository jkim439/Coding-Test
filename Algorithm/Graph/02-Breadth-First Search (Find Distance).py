def bfs(n, m, map):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    queue = [[0, 0]]

    while queue:
        y, x = queue.pop(0)

        for i in range(4):
            ny, nx = [y + dy[i], x + dx[i]]

            if (
                0 <= ny < n
                and 0 <= nx < m
                and visited[ny][nx] == 0
                and map[ny][nx] == 1
            ):
                visited[ny][nx] = visited[y][x] + 1
                queue.append([ny, nx])

    return visited[n - 1][m - 1]


print(
    bfs(
        4,
        6,
        [
            [1, 0, 1, 1, 1, 1],
            [1, 0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1, 1],
            [1, 1, 1, 0, 1, 1],
        ],
    )
)
