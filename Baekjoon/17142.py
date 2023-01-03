# 연구소 3 (미완성)
def bfs(n, m, start, graph):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    visited = [[None] * n for _ in range(n)]
    queue = [] + start

    result = -1

    for s in start:
        visited[s[0]][s[1]] = 0

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

    return result


def combinations(m, data, comb, depth):

    global answer

    if len(comb) == m:
        val = bfs(n, m, comb, graph)
        answer = min(answer, val)
        return
    if len(data) == depth:
        return

    comb.append(data[depth])
    combinations(m, data, comb, depth + 1)

    comb.pop()
    combinations(m, data, comb, depth + 1)


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

virus = []
for r in range(n):
    for c in range(n):
        if graph[r][c] == 2:
            virus.append([r, c])

answer = 99999
combinations(m, virus, list(), 0)
print(answer)
