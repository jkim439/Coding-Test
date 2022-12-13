# 메뉴 리뉴얼
from collections import Counter
from itertools import combinations


def solution(orders, course):
    answer = []

    for c in course:
        temp = []
        for o in orders:
            temp += combinations(sorted(o), c)
        counter = Counter(temp)
        if len(counter) != 0 and max(counter.values()) != 1:
            answer += [
                "".join(s) for s in counter if counter[s] == max(counter.values())
            ]

    return sorted(answer)
