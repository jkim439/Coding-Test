def get_block(d, i):
    if d == 0:
        if i == 1:
            return [0, 3]
        elif i == 3:
            return [0, 4]
    if d == 1:
        if i == 0:
            return [1, 5]
        elif i == 2:
            return [1, 4]
    if d == 2:
        if i == 1:
            return [2, 6]
        elif i == 3:
            return [2, 5]
    if d == 3:
        if i == 0:
            return [3, 6]
        elif i == 2:
            return [3, 3]


def bfs(n, board):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    visited = [[0] * n for _ in range(n)]
    visited[n - 1][n - 1] = 1

    record = [[[0]] * n for _ in range(n)]
    queue = [[n - 1, n - 1, 3]]

    while queue:
        y, x, d = queue.pop(0)

        if [y, x] == [0, 0]:
            return visited

        if 1 <= board[y][x] <= 2:
            ny, nx = y + dy[d], x + dx[d]
            if d == 1 or d == 3:
                b = 1
            else:
                b = 2
            if (
                0 <= ny < n
                and 0 <= nx < n
                and [d, b] not in record[y][x]
                and board[ny][nx] != 0
            ):
                visited[ny][nx] = visited[y][x] + 1
                queue.append([ny, nx, d])
                if record[y][x] == [0]:
                    record[y][x] = list()
                record[y][x].append([d, b])

        if 3 <= board[y][x] <= 6:
            for i in [(d + 1) % 4, (d + 3) % 4]:
                ny, nx = y + dy[i], x + dx[i]

                if (
                    0 <= ny < n
                    and 0 <= nx < n
                    and get_block(d, i) not in record[y][x]
                    and board[ny][nx] != 0
                ):
                    visited[ny][nx] = visited[y][x] + 1
                    queue.append([ny, nx, i])
                    if record[y][x] == [0]:
                        record[y][x] = list()
                    record[y][x].append(get_block(d, i))


##################################################
import sys

sys.stdin = open(sys.argv[0][:-3] + ".txt", "r")
##################################################
for t in range(1, int(input()) + 1):
    n = int(input())
    b = [list(map(int, input().split())) for _ in range(n)]
    print(f"#{t} {bfs(n, b)}")
