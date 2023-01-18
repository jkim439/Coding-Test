# 최고의 집합
def solution(n, s):
    answer = []
    while n > 0:
        v = s // n
        if v == 0:
            return [-1]
        answer.append(v)
        s -= v
        n -= 1
    return answer
