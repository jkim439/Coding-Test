# 칩 생산
def dfs(y, x, count, idx):
    global answer
    answer = max(answer, count)
    if h - 1 <= y:
        if count <= dp[idx][x]:
            return
        else:
            dp[idx][x] = count
        dfs(0, x + 1, count, 0)
        return
    if w - 1 <= x:
        return
    if (
        maps[y][x] == 0
        and maps[y][x + 1] == 0
        and maps[y + 1][x] == 0
        and maps[y + 1][x + 1] == 0
    ):
        maps[y][x] = maps[y + 1][x] = maps[y][x + 1] = maps[y + 1][x + 1] = 1
        dfs(y + 2, x, count + 1, (idx | 1 << y))
        maps[y][x] = maps[y + 1][x] = maps[y][x + 1] = maps[y + 1][x + 1] = 0
    dfs(y + 1, x, count, idx)


for t in range(1, int(input()) + 1):
    h, w = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(h)]

    answer = 0
    dp = [[-1] * w for _ in range(1 << h)]
    dfs(0, 0, 0, 0)

    print(f"#{t} {answer}")
