# 예상 대진표
def solution(n, a, b):
    answer = 0

    while True:
        answer += 1
        a1 = a // 2
        b1 = b // 2
        a2 = (a + 1) // 2
        b2 = (b + 1) // 2
        if abs(a1 - b1) == 1 and a2 == b2:
            return answer
        else:
            a = a2
            b = b2
