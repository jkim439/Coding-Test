# 아기 상어 (미완성)
##################################################
import sys

sys.stdin = open(sys.argv[0][:-3] + ".txt", "r")
##################################################
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
s = 2

fish = []
for r in range(n):
    for c in range(n):
        if 0 < graph[r][c] < s:
            fish.append([r, c])
        elif graph[r][c] == 9:
            shark = [r, c]

answer = 0
print(fish)
while fish:

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    queue = [shark]

    visited = [[0] * n for _ in range(n)]
    visited[shark[0]][shark[1]] = 0

    while queue:
        y, x = queue.pop(0)

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if (
                0 <= ny < n
                and 0 <= nx < n
                and graph[ny][nx] <= s
                and visited[ny][nx] == 0
                and [ny, nx] != shark
            ):
                visited[ny][nx] = visited[y][x] + 1
                queue.append([ny, nx])

    for f in fish:
        f.append(visited[f[0]][f[1]])

    fish.sort(key=lambda x: (x[2], x[0], x[1]))

    print(fish)
    fy, fx, d = fish.pop(0)
    shark = [fy, fx]
    s += 1
    graph[fy][fx] = 0

    fish = []
    for r in range(n):
        for c in range(n):
            if 0 < graph[r][c] < s:
                fish.append([r, c])

    answer += d

print(answer)
