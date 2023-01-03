# [1차] 프렌즈4블록
def solution(m, n, board):
    b = [[] for _ in range(len(board[0]))]

    for c in range(len(board[0])):
        for r in range(len(board)):
            b[c].append(board[r][c])

    answer = 0
    run = True
    while run is True:
        run = False

        for i in range(1, len(b)):
            for j in range(1, len(b[i])):
                if b[i][j] == "#":
                    continue
                b_char = b[i][j]
                b_star = b_char + "*"
                if (
                    (b[i - 1][j - 1] == b_char or b[i - 1][j - 1] == b_star)
                    and (b[i - 1][j] == b_char or b[i - 1][j] == b_star)
                    and (b[i][j - 1] == b_char or b[i][j - 1] == b_star)
                ):
                    b[i][j] = b[i - 1][j - 1] = b[i - 1][j] = b[i][j - 1] = b_star
                    run = True

        for r in range(len(b)):
            answer += len([c for c in b[r] if c.isalpha() == False and c != "#"])
            remove = [c for c in b[r] if c.isalpha() == False]
            b[r] = [c for c in b[r] if c.isalpha() == True]

            for _ in range(len(remove)):
                b[r].insert(0, "#")

    return answer
