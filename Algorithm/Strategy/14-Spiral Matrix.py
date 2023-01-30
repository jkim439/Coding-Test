def spiral_matrix(n):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    y = x = n // 2
    d = m = i = 0
    j = 1

    graph = [[0] * n for _ in range(n)]

    while 1:
        m += 1

        for _ in range(j):
            ny, nx = y + dy[d], x + dx[d]

            if [ny, nx] == [0, -1]:
                return graph

            i += 1
            graph[ny][nx] = i
            y, x = ny, nx

        if m == 2:
            m = 0
            j += 1

        d = (d + 1) % 4


print(spiral_matrix(7))
