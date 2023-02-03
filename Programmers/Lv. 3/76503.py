# 모두 0으로 만들기
import sys

sys.setrecursionlimit(300000)
from collections import defaultdict


def dfs(x, a, tree, visited):
    global answer

    visited[x] = 1
    for y in tree[x]:
        if visited[y] == 0:
            a[x] += dfs(y, a, tree, visited)

    answer += abs(a[x])

    return a[x]


def solution(a, edges):
    global answer
    answer = 0

    if sum(a) != 0:
        return -1

    tree = defaultdict(list)
    for x, y in edges:
        tree[x].append(y)
        tree[y].append(x)

    visited = [0] * len(a)
    dfs(0, a, tree, visited)

    return answer
