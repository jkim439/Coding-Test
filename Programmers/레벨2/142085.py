from itertools import combinations


def solution(n, k, enemy):
    answer = 0
    combination = list(combinations(list(range(len(enemy))), k))
    return combination


print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]))
