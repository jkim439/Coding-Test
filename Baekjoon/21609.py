from collections import deque


def bfs(n, y, x, c, graph):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    queue = deque()
    queue.append([y, x])

    blocks = [] if c == 0 else [[y, x]]
    rainbows = [[y, x]] if c == 0 else []

    normal = 0 if c == 0 else 1
    rainbow = 1 if c == 0 else 0
    min_y = 9999
    min_x = 9999

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if 0 <= ny < n and 0 <= nx < n and visited[ny][nx] == 0:
                if graph[ny][nx] == 0:
                    visited[ny][nx] = 1
                    rainbow += 1
                    queue.append([ny, nx])
                    rainbows.append([ny, nx])
                elif graph[ny][nx] > 0 and c == 0:
                    c = graph[ny][nx]
                    visited[ny][nx] = 1
                    normal += 1
                    queue.append([ny, nx])
                    blocks.append([ny, nx])
                elif graph[ny][nx] == c and c != 0:
                    visited[ny][nx] = 1
                    normal += 1
                    queue.append([ny, nx])
                    blocks.append([ny, nx])

                if c != 0:
                    if ny < min_y and nx < min_x:
                        min_y = ny
                        min_x = nx
                    elif ny < min_y and nx <= min_x:
                        min_y = ny
                        min_x = nx
                    elif ny <= min_y and nx < min_x:
                        min_y = ny
                        min_x = nx

    for y, x in rainbows:
        visited[y][x] = 0

    if normal > 0 and (normal + rainbow) >= 2:
        return [(normal + rainbow), rainbow, min_y, min_x, blocks + rainbows]
    else:
        return None


def gravity(n, graph):
    for r in range(n - 1):
        for c in range(n):
            if graph[r][c] >= 0:
                rs = r + 1
                while rs < n - 1 and graph[rs][c] >= 0:
                    rs += 1
                re = rs
                while re < n and graph[re][c] == -2:
                    re += 1
                i_add = re - rs
                if rs < re:
                    for i in range(rs - 1, r - 1, -1):
                        i_add = i + re - rs
                        graph[i_add][c] = graph[i][c]
                        graph[i][c] = -2

    return graph


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

score = 0

while 1:
    bfs_result = []
    visited = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if graph[r][c] == 0 and visited[r][c] == 0:
                visited[r][c] = 1
                result = bfs(n, r, c, 0, graph)
                if result is not None:
                    bfs_result.append(result)
            elif graph[r][c] > 0 and visited[r][c] == 0:
                visited[r][c] = 1
                result = bfs(n, r, c, graph[r][c], graph)
                if result is not None:
                    bfs_result.append(result)

    if len(bfs_result) < 1:
        break

    bfs_result.sort(key=lambda x: (-x[0], -x[1], -x[2], -x[3]))
    block = bfs_result[0]

    # 2. 찾은 블록 그룹의 모든 블록 제거하고 점수 획득
    for y, x in block[4]:
        graph[y][x] = -2
    score += block[0] ** 2

    # 3. 중력 작용
    graph = gravity(n, graph)

    # 4. 90도 반시계 방향 회전
    graph = list(zip(*graph))[::-1]
    graph = [list(i) for i in graph]

    # 5. 중력 작용
    graph = gravity(n, graph)

    print(score, graph)
