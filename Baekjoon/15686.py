# 치킨 배달
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

house = []
chicken = []
for r in range(n):
    for c in range(n):
        if graph[r][c] == 1:
            house.append([r, c])
        elif graph[r][c] == 2:
            chicken.append([r, c])


def combinations(m, data, comb, depth):
    global answer
    if len(comb) == m:

        city = 0
        for h in house:
            v = 99999
            for c in comb:
                v = min(v, abs(c[0] - h[0]) + abs(c[1] - h[1]))
            city += v
        answer = min(answer, city)

        return
    if len(data) == depth:
        return

    comb.append(data[depth])
    combinations(m, data, comb, depth + 1)

    comb.pop()
    combinations(m, data, comb, depth + 1)


answer = 99999
combinations(m, chicken, list(), 0)
print(answer)
