# 롤케이크 자르기
from collections import Counter


def solution(topping):
    answer = 0
    t1 = Counter(topping)
    t2 = set()

    for t in topping:
        t1[t] -= 1
        t2.add(t)

        if t1[t] == 0:
            t1.pop(t)

        if len(t1) == len(t2):
            answer += 1

    return answer
