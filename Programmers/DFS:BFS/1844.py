# 게임 맵 최단거리
from collections import deque


def solution(maps):
    y = len(maps) - 1
    x = len(maps[0]) - 1
    visited = [[0] * (x + 1) for _ in range(y + 1)]
    direction = ((-1, 0), (1, 0), (0, -1), (0, 1))

    queue = deque()
    queue.append((0, 0, 1))
    while queue:
        r, c, s = queue.popleft()
        visited[r][c] = 1

        for i in range(4):
            row, col, step = r + direction[i][0], c + direction[i][1], s + 1
            if row == y and col == x:
                return step
            if (
                row < 0
                or col < 0
                or y < row
                or x < col
                or visited[row][col] != 0
                or maps[row][col] != 1
            ):
                continue
            queue.append((row, col, step))
            visited[row][col] = 1

    return -1
