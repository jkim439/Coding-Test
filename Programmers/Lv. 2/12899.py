# 124 나라의 숫자
def solution(n):
    answer = ""
    array = ["1", "2", "4"]
    while 0 < n:
        n -= 1
        answer = array[n % 3] + answer
        n //= 3
    return answer
