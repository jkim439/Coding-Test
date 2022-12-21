# 귤 고르기
from collections import Counter


def solution(k, tangerine):
    box = []
    for t in Counter(tangerine).most_common():
        if k <= len(box):
            break
        else:
            for _ in range(t[1]):
                box.append(t[0])

    return len(set(box))
