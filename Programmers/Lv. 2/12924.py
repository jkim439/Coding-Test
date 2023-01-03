# 숫자의 표현
def solution(n):
    answer = 0
    for i in range(1, n + 1):
        j = i
        k = i
        while k < n:
            j += 1
            k += j
        if k == n:
            answer += 1
            continue
    return answer
