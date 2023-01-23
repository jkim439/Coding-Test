# 1257. [S/W 문제해결 응용] 6일차 - K번째 문자열
for t in range(1, int(input()) + 1):
    k = int(input())
    s = str(input())
    a = []

    for l in range(1, len(s) + 1):
        for i in range(len(s)):
            if i + l <= len(s):
                a.append(s[i : i + l])

    a = list(set(a))
    a.sort()

    if k - 1 < 0 or k - 1 > len(a) - 1:
        print(f"#{t} none")
    else:
        print(f"#{t} {a[k - 1]}")
