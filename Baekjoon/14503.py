# 로봇 청소기
n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]

answer = 0
error = 0

while 1:

    # 현 위치 청소
    if graph[r][c] == 0:
        graph[r][c] = 2
        answer += 1

    # 네 방향 시도
    if error < 4:

        # 왼쪽 방향 청소 여부 확인
        ny, nx = r + dy[d % 4], c + dx[d % 4]
        if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == 0:
            d = (d + 3) % 4
            error = 0
            r, c = ny, nx

        else:
            d = (d + 3) % 4
            error += 1

    # 네 방향 실패
    else:
        by, bx = r + dy[(d + 3) % 4], c + dx[(d + 3) % 4]
        if graph[by][bx] == 1:
            print(answer)
            break

        else:
            r, c = by, bx
            error = 0
