n = 5
board = []

# 보드판 생성
i = 0
for _ in range(n):
    board.append([i for i in range(i, i + n)])
    i += n
print(board)

# 원하는 부위 복사하여 회전
temp = []
for r in range(1, 4):
    temp.append(board[r][1:4])
temp = list(map(list, zip(*board[::-1])))
print(temp)

# 회전한 결과를 원래 보드판에 붙여넣기
for r in range(1, 4):
    board[r][1:4] = temp[r - 1]
print(board)
