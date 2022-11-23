# 네트워크
def solution(n, computers):
    answer = 0
    visited = [0 for i in n]
    for i in range(n):
        if visited[i] == 0:
            dfs(i, visited, n, computers)
            answer += 1
    return answer


def dfs(i, visited, n, computers):
    visited[i] = 1
    for j in range(n):
        if computers[i][j] != 0 and visited[j] == 0:
            dfs(j, visited, n, computers)
