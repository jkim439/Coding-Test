# 줄 서는 방법
from math import factorial


def solution(n, k):
    data = [i for i in range(1, n + 1)]
    stack = []
    k -= 1

    while data:
        i = k // factorial(n - 1)
        stack.append(data[i])
        del data[i]

        k %= factorial(n - 1)
        n -= 1

    return stack
