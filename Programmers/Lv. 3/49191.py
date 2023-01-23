# 순위
from collections import defaultdict


def solution(n, results):
    answer = 0
    win, lose = defaultdict(set), defaultdict(set)

    for w, l in results:
        win[w].add(l)
        lose[l].add(w)

    for i in range(1, n + 1):
        for l in win[i]:
            lose[l].update(lose[i])
        for w in lose[i]:
            win[w].update(win[i])

    for i in range(1, n + 1):
        if len(win[i]) + len(lose[i]) == n - 1:
            answer += 1

    return answer
