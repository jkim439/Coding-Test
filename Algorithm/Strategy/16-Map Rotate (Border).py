n = 7
board = []

# 보드판 생성
i = 0
for _ in range(n):
    board.append([i for i in range(i, i + n)])
    i += n
print(board)

# 원하는 테두리 포함 전체 범위 복사하여 회전
temp1 = []
for r in range(1, 6):
    temp1.append(board[r][1:6])
temp1 = list(zip(*temp1[::-1]))
print(temp1)

# 원치 않는 테두리 제외하고 내부 범위 복사
temp2 = []
for r in range(2, 5):
    temp2.append(board[r][2:5])
print(temp2)

# 회전한 결과를 원래 보드판에 붙여넣고, 테두리 제외한 내부 범위 보드판에 붙여넣기
for r in range(1, 6):
    board[r][1:6] = temp1[r - 1]
for r in range(2, 5):
    board[r][2:5] = temp2[r - 2]
print(board)
