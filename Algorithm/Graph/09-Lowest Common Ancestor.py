# Root Node부터 출발하여 깊이를 구하는 함수
def dfs(i, depth):
    c[i] = True
    d[i] = depth

    for j in adjacent[i]:
        if not c[j]:
            parent[j][0] = i
            dfs(j, depth + 1)


# Lowest Common Ancestor
def lca(a, b):
    # B가 더 깊도록 설정
    if d[a] > d[b]:
        a, b = b, a

    # 깊이가 동일하도록
    for i in range(log - 1, -1, -1):
        if d[b] - d[a] >= (1 << i):
            b = parent[b][i]

    # 부모가 같아지도록
    if a == b:
        return a

    # 조상을 향해 거슬러 올라가기
    for i in range(log - 1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]

    # 부모가 찾고자 하는 조상
    return parent[a][0]


n = int(input())
adjacent = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    adjacent[a].append(b)
    adjacent[b].append(a)

c = [0] * (n + 1)  # 각 노드 깊이가 계산되었는지 여부
d = [0] * (n + 1)  # 각 노드까지의 깊이
log = 21  # 2^20 = 1,000,000

parent = [[0] * log for _ in range(n + 1)]  # 부모 노드 정보
dfs(1, 0)  # 1번(Root Node)부터 시작

for i in range(1, log):
    for j in range(1, n + 1):
        parent[j][i] = parent[parent[j][i - 1]][i - 1]

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))

"""
[INPUT]
15
1 2
1 3
2 4
3 7
6 2
3 8
4 9
2 5
5 11
7 13
10 4
11 15
12 5
14 7
6
6 11
10 9
2 6
7 6
8 13
8 15

[OUTPUT]
2
4
2
1
3
1
"""
