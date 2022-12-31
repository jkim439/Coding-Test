# 숫자 카드 나누기
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def solution(arrayA, arrayB):
    answer = []

    gcdA = arrayA[0]
    gcdB = arrayB[0]

    for a, b in zip(arrayA[1:], arrayB[1:]):
        gcdA = gcd(gcdA, a)
        gcdB = gcd(gcdB, b)

    for a in arrayA:
        if a % gcdB == 0:
            break
    else:
        answer.append(gcdB)

    for b in arrayB:
        if b % gcdA == 0:
            break
    else:
        answer.append(gcdA)

    return max(answer) if answer else 0
