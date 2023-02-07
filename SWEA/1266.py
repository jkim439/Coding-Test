# 1266. [S/W 문제해결 응용] 9일차 - 소수 완제품 확률
from math import factorial


def nCr(n, r):
    return factorial(n) // factorial(r) // factorial(n - r)


nonprime = [0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18]
for t in range(1, int(input()) + 1):
    a, b = map(int, input().split())
    a /= 100
    b /= 100

    a_prob = []
    b_prob = []

    for n in nonprime:
        a_prob.append((a**n) * ((1 - a) ** (18 - n)) * nCr(18, n))
        b_prob.append((b**n) * ((1 - b) ** (18 - n)) * nCr(18, n))

    answer = 1 - sum(a_prob) * sum(b_prob)
    print(f"#{t} {answer:.6f}")
