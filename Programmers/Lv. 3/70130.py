# 스타 수열
from collections import Counter


def solution(a):
    if len(a) == 1:
        return 0

    answer = -1

    c = Counter(a)
    for k, v in c.items():
        if c[k] * 2 < answer:
            continue

        i = 0
        count = 0
        while i < len(a) - 1:
            if (a[i] != k and a[i + 1] != k) or a[i] == a[i + 1]:
                i += 1
                continue
            i += 2
            count += 2

        answer = max(answer, count)

    return answer
