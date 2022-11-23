from functools import cmp_to_key


def comparator(a, b):
    x = int(a + b)
    y = int(b + a)
    print("comparator", a, b, x, y, (x > y) - (x < y))
    return (x > y) - (x < y)


def solution(numbers):
    answer = numbers
    answer = list(map(str, answer))
    print(answer)
    answer = sorted(answer, key=cmp_to_key(comparator), reverse=True)
    print(answer)
    answer = "".join(answer)
    print(answer)


solution([3, 30, 34, 5, 9])  # 9534330
