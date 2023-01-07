# 검은색 블록(-1)을 제외한 모든 블록이 아래 방향으로 이동
def gravity(n, board):
    for i in range(n - 2, -1, -1):
        for j in range(n):
            if board[i][j] != -1:
                k = i

                # 다음 칸이 끝이 아니면서 빈칸(-2)인 경우 중력으로 떨어짐
                while k + 1 < n and board[k + 1][j] == -2:
                    board[k + 1][j] = board[k][j]
                    board[k][j] = -2
                    k += 1
