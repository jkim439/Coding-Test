# 양궁대회
from itertools import combinations_with_replacement


def solution(n, info):
    a = info[::-1]
    board = list(range(11))

    combinations = list(combinations_with_replacement(board, n))

    answer = list()
    difference = 0

    for combination in combinations:
        r = [0] * 11
        for c in combination:
            r[c] += 1

        a_score = 0
        r_score = 0
        for i in range(11):
            if a[i] >= r[i] and a[i] != 0:
                a_score += i
            elif a[i] <= r[i] and r[i] != 0:
                r_score += i

        if r_score > a_score:
            if len(answer) == 0 and difference == 0:
                answer = list()
                answer.append(r)
                difference = r_score - a_score
            else:
                if difference < r_score - a_score:
                    answer = list()
                    answer.append(r)
                    difference = r_score - a_score
                elif difference == r_score - a_score:
                    answer.append(r)

    if len(answer) > 0:
        answer.sort(reverse=True)
        return (answer[0])[::-1]
    else:
        return [-1]
