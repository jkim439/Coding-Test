def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def solution(w, h):
    answer = gcd(w, h)
    return answer


print(solution(8, 12))
