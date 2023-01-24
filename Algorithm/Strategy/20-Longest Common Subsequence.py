def lcs(m, n):
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
            else:
                c[i][j] = max(c[i - 1][j], c[i][j - 1])
    return c[m][n]


a = input()
b = input()
m = len(a)
n = len(b)
c = [[0] * (n + 1) for _ in range(m + 1)]
print(lcs(m, n))

"""
[INPUT]
RBKBGRBGGG
BGKRBRKBGB

[OUTPUT]
6
"""
