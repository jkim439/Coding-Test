# 1267. [S/W 문제해결 응용] 10일차 - 작업순서
for t in range(1, 11):
    n, e = map(int, input().split())
    adjacent = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)

    s = input().split()
    for i in range(0, e * 2, 2):
        a, b = int(s[i]), int(s[i + 1])
        adjacent[a].append(b)
        indegree[b] += 1

    answer = []
    queue = []

    for i in range(1, n + 1):
        if not indegree[i]:
            queue.append(i)

    for _ in range(1, n + 1):
        i = queue.pop(0)
        answer.append(i)

        for j in adjacent[i]:
            indegree[j] -= 1
            if not indegree[j]:
                queue.append(j)

    answer = " ".join(map(str, answer))

    print(f"#{t} {answer}")
