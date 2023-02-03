# 1264. [S/W 문제해결 응용] 8일차 - 이미지 유사도 검사
for t in range(1, int(input()) + 1):
    l = int(input())
    a = str(input())
    b = str(input())
    c = [[0] * (l + 1) for _ in range(l + 1)]

    for i in range(1, l + 1):
        for j in range(1, l + 1):
            if a[i - 1] == b[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
            else:
                c[i][j] = max(c[i - 1][j], c[i][j - 1])

    answer = float(c[l][l] / l) * 100
    print(f"#{t} {answer:.2f}")
