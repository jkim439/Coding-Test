def dfs(r, n, queen):
    count = 0

    if r == n:
        return 1

    for c in range(n):
        queen[r] = c

        for r0 in range(r):
            if queen[r] == queen[r0] or abs(queen[r] - queen[r0]) == abs(r - r0):
                break
        else:
            count += dfs(r + 1, n, queen)

    return count


n = 5
queen = [0] * n
print(dfs(0, n, queen))
