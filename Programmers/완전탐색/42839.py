# 소수 찾기
from itertools import permutations


def is_prime(number):
    if number <= 1:
        return 0
    else:
        for num in range(2, number):
            if number % num == 0:
                return 0
        return 1


def solution(numbers):
    numbers = [n for n in numbers]
    permutation = []
    for i in range(1, len(numbers) + 1):
        permutation += list(permutations(numbers, i))
    permutation = list(set([int("".join(p)) for p in permutation]))
    answer = 0
    for number in permutation:
        answer += is_prime(number)
    return answer
