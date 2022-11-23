# N개의 최소공배수
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b / gcd(a, b)


def solution(arr):
    for i in range(len(arr) - 1):
        if i == 0:
            c = lcm(arr[i], arr[i + 1])
        else:
            c = lcm(c, arr[i + 1])
    return c
