# 행렬 테두리 회전하기
def solution(rows, columns, queries):
    answer = []

    matrix = []
    n = 1
    for _ in range(rows):
        matrix.append([i for i in range(n, n + columns)])
        n += columns

    for query in queries:
        sr, sc, er, ec = [i - 1 for i in query]
        ans = matrix[sr][sc]
        temp = ans

        for r in range(sr + 1, er + 1):
            matrix[r - 1][sc] = matrix[r][sc]
            ans = min(ans, matrix[r][sc])

        for c in range(sc + 1, ec + 1):
            matrix[er][c - 1] = matrix[er][c]
            ans = min(ans, matrix[er][c])

        for r in range(er - 1, sr - 1, -1):
            matrix[r + 1][ec] = matrix[r][ec]
            ans = min(ans, matrix[r][ec])

        for c in range(ec - 1, sc - 1, -1):
            matrix[sr][c + 1] = matrix[sr][c]
            ans = min(ans, matrix[sr][c])

        matrix[sr][sc + 1] = temp

        answer.append(ans)

    return answer
