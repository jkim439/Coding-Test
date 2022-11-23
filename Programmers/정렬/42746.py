# 가장 큰 수
from functools import cmp_to_key


def comparator(a, b):
    x = int(a + b)
    y = int(b + a)
    return (x > y) - (x < y)


def solution(numbers):
    return str(
        int(
            "".join(
                sorted(
                    list(map(str, numbers)), key=cmp_to_key(comparator), reverse=True
                )
            )
        )
    )
