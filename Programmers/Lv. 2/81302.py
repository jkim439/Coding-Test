# 거리두기 확인하기
from collections import deque


def bfs(graph, y, x):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    visited = [[0] * 5 for _ in range(5)]
    visited[y][x] = 1

    queue = deque()
    queue.append([y, x])

    while queue:
        y, x = queue.popleft()

        if visited[y][x] > 2:
            return True

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if 0 <= ny < 5 and 0 <= nx < 5 and visited[ny][nx] == 0:
                if graph[ny][nx] == "O":
                    visited[ny][nx] = visited[y][x] + 1
                    queue.append([ny, nx])
                elif graph[ny][nx] == "X":
                    continue
                elif graph[ny][nx] == "P":
                    return False


def solution(places):
    answer = []

    for place in places:
        for i in range(len(place)):
            place[i] = list(place[i])

        breaker = False
        for r in range(5):
            for c in range(5):
                if breaker is True:
                    break
                if place[r][c] == "P":
                    bfs_result = bfs(place, r, c)
                    if bfs_result is False:
                        answer.append(0)
                        breaker = True
                        break
            if breaker is True:
                break

        if breaker is False:
            answer.append(1)

    return answer
