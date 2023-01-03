# 최솟값 만들기
def solution(A, B):
    sum = 0
    A.sort()
    B.sort(reverse=True)
    while A:
        sum += A.pop() * B.pop()
    return sum
