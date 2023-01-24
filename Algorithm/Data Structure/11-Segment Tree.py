from math import ceil, log2


def sum(start, end, left, right, i):
    if start > right or left > end:
        return 0
    if start >= left and right >= end:
        return tree[i]
    mid = (start + end) // 2
    return sum(start, mid, left, right, i * 2) + sum(
        mid + 1, end, left, right, i * 2 + 1
    )


def update(i, diff):
    j = size + i - 1
    while j >= 1:
        tree[j] += diff
        j //= 2


n, m, k = map(int, input().split())
size = 2 ** ceil(log2(n))
tree = [0] * (size * 2)

for i in range(n):
    tree[size + i] = int(input())

for i in range(size - 1, 0, -1):
    tree[i] = tree[i * 2] + tree[i * 2 + 1]

for i in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        diff = c - tree[size + b - 1]
        update(b, diff)
    else:
        print(sum(1, size, b, c, 1))


"""
[INPUT]
5 2 2
1
2
3
4
5
1 3 6
2 2 5
1 5 2
2 3 5

[OUTPUT]
17
12
"""
