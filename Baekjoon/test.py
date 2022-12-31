from collections import deque

# 인접 블록 찾기 -> 블록 크기, 무지개크기, 블록좌표 리턴
def bfs(x, y, color):
    q = deque()
    q.append([x, y])
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    block_cnt, rainbow_cnt = 1, 0  # 블록개수, 무지개블록 개수
    blocks, rainbows = [[x, y]], []  # 블록좌표 넣을 리스트, 무지개좌표 넣을 리스트

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            # 범위 안이면서 방문 안한 일반 블록인 경우
            if (
                0 <= nx < n
                and 0 <= ny < n
                and not visited[nx][ny]
                and graph[nx][ny] == color
            ):
                visited[nx][ny] = 1
                q.append([nx, ny])
                block_cnt += 1
                blocks.append([nx, ny])

            # 범위 안이면서 방문 안한 무지개 블록인 경우
            elif (
                0 <= nx < n
                and 0 <= ny < n
                and not visited[nx][ny]
                and graph[nx][ny] == 0
            ):
                visited[nx][ny] = 1
                q.append([nx, ny])
                block_cnt += 1
                rainbow_cnt += 1
                rainbows.append([nx, ny])

    # 무지개블록은 방문 다시 해제
    for x, y in rainbows:
        visited[x][y] = 0

    return [block_cnt, rainbow_cnt, blocks + rainbows]


# 블록 제거 함수
def remove(block):
    for x, y in block:
        graph[x][y] = -2


# 중력 함수
def gravity(graph):
    for i in range(n - 2, -1, -1):  # 밑에서 부터 체크
        for j in range(n):
            if graph[i][j] > -1:  # -1이 아니면 아래로 다운
                r = i
                while True:
                    if (
                        0 <= r + 1 < n and graph[r + 1][j] == -2
                    ):  # 다음행이 인덱스 범위 안이면서 -2이면 아래로 다운
                        graph[r + 1][j] = graph[r][j]
                        graph[r][j] = -2
                        r += 1
                    else:
                        break


# 반시계 회전 함수
def rot90(graph):
    new_a = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_a[n - 1 - j][i] = graph[i][j]
    return new_a


# 0. 메인코드
n, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

score = 0  # 점수

# 1. 오토플레이-> while {2. 크기 가장 큰 블록 찾기 3. 블록제거+점수더하기 4. 중력 5. 90회전 6. 중력}
while True:

    print("1", graph)
    # 2. 크기 가장 큰 블록 찾기
    visited = [[0] * n for _ in range(n)]  # 방문체크
    blocks = []  # 가능한 블록 그룹들 넣을 리스트
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0 and not visited[i][j]:  # 일반블록이면서 방문 안했으면
                visited[i][j] = 1  # 방문
                block_info = bfs(i, j, graph[i][j])  # 인접한 블록 찾기
                # block_info = [블록크기, 무지개블록 개수, 블록좌표]
                if block_info[0] >= 2:
                    blocks.append(block_info)
    blocks.sort(reverse=True)

    # 3. 블록제거+점수더하기
    if not blocks:
        break
    remove(blocks[0][2])
    score += blocks[0][0] ** 2
    print("2", graph, score)

    # 4. 중력
    gravity(graph)
    print("3", graph)

    # 5. 90회전
    graph = rot90(graph)
    print("4", graph)

    # 6. 중력
    gravity(graph)
    print("5", graph)
print(score)
