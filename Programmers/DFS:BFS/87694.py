# 아이템 줍기
def solution(rectangle, characterX, characterY, itemX, itemY):

    # 2배 큰 필드 생성
    max = 51 * 2
    field = [[0] * max for _ in range(max)]

    # 직사각형 채우기 (테두리: 2, 내부: 1)
    for rec in rectangle:
        x1, y1, x2, y2 = map(lambda x: x * 2, rec)
        for c in range(x1, x2 + 1):
            for r in range(y1, y2 + 1):
                if (field[r][c] != 1) and (r == y1 or r == y2 or c == x1 or c == x2):
                    field[r][c] = 2
                else:
                    field[r][c] = 1

    # BFS
    count = 0
    visited = []
    queue = []
    queue.append([characterX * 2, characterY * 2])

    while queue:
        count += 1
        node = queue.pop(0)
        x, y = node

        if x == itemX * 2 and y == itemY * 2:
            return count // 4

        if node not in visited:
            visited.append(node)

            if field[y][x - 1] == 2 and [x - 1, y] not in visited:
                queue.append([x - 1, y])
            if field[y][x + 1] == 2 and [x + 1, y] not in visited:
                queue.append([x + 1, y])
            if field[y - 1][x] == 2 and [x, y - 1] not in visited:
                queue.append([x, y - 1])
            if field[y + 1][x] == 2 and [x, y + 1] not in visited:
                queue.append([x, y + 1])

    return visited
