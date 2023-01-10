# 오래된 스마트폰
def calculate(n1, n2, oper):
    if oper == 1:
        n1 += n2
    elif oper == 2:
        n1 -= n2
    elif oper == 3:
        n1 *= n2
    else:
        if n2 == 0:
            return -1
        else:
            n1 //= n2
    if 0 <= n1 < 1000:
        return n1
    else:
        return -1


def candidate(n, x):
    if n == 3:
        return
    for k in keys:
        i = x * 10 + k
        if visited[i] <= n + 1:
            continue
        visited[i] = n + 1
        queue.append(i)
        nums.append(i)
        candidate(n + 1, i)


for t in range(1, int(input()) + 1):
    n, o, m = map(int, input().split())
    keys = list(map(int, input().split()))
    opers = list(map(int, input().split()))
    w = int(input())

    queue = []
    visited = [float("inf") for _ in range(1000)]

    nums = []
    candidate(0, 0)

    if visited[w] < float("inf"):
        print(f"#{t} {visited[w]}")
        continue

    while queue:
        v = queue.pop(0)
        for n in nums:
            click = visited[v] + len(str(n)) + 1
            if click + 1 > m:
                continue
            for oper in opers:
                i = calculate(v, n, oper)
                if i == -1:
                    continue
                if visited[i] <= click:
                    continue
                visited[i] = click
                queue.append(i)

    if visited[w] < float("inf"):
        print(f"#{t} {visited[w] + 1}")
    else:
        print(f"#{t} -1")
