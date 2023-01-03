# 피로도
from itertools import permutations


def solution(k, dungeons):
    cases = list(permutations(dungeons, len(dungeons)))
    answer = 0

    while cases:
        case = cases.pop()

        n = 0
        remained = k
        case = list(case)

        while case:
            required, spent = case.pop()
            if remained >= required:
                remained -= spent
                n += 1
        if n > answer:
            answer = n

    return answer
