def topological_sort():
    n = int(input())
    adjacent = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)

    for _ in range(n):
        a, b = map(int, input().split())
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

    return answer


print(topological_sort())

"""
[INPUT]
7
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4

[OUTPUT]
[1, 2, 5, 3, 6, 4, 7]
"""
