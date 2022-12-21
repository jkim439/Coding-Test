from itertools import combinations


def bfs(n, start, graph):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    visited = [[None] * n for _ in range(n)]
    queue = []

    result = 0

    for y, x in start:
        queue.append([y, x])
        visited[y][x] = 0

    while queue:

        y, x = queue.pop(0)

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if 0 <= ny < n and 0 <= nx < n and visited[ny][nx] is None:
                if graph[ny][nx] == 0:
                    visited[ny][nx] = visited[y][x] + 1
                    queue.append([ny, nx])
                    result = max(result, visited[ny][nx])

                elif graph[ny][nx] == 2:
                    visited[ny][nx] = visited[y][x] + 1
                    queue.append([ny, nx])

    if list(sum(visited, [])).count(-1) != wall_cnt:
        return inf
    return result


# def combinations(m, data, comb, depth):

#     global answer

#     if len(comb) == m:
#         val = bfs(n, comb, graph)
#         print(comb, val)
#         answer = min(answer, val)
#         return
#     if len(data) == depth:
#         return

#     comb.append(data[depth])
#     combinations(m, data, comb, depth + 1)

#     comb.pop()
#     combinations(m, data, comb, depth + 1)


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

wall_cnt = 0
virus = []
for r in range(n):
    for c in range(n):
        if graph[r][c] == 1:
            wall_cnt += 1
        elif graph[r][c] == 2:
            virus.append([r, c])

import sys

inf = sys.maxsize

# combinations(m, virus, list(), 0)
ans = inf
for c in combinations(virus, m):
    ans = min(ans, bfs(n, c, graph))

print(ans if ans != inf else -1)
