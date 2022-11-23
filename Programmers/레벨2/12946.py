# 하노이의 탑
def tower_of_hanoi(start, end, n, answer):
    if n == 1:
        answer.append([start, end])
    else:
        empty = 6 - start - end
        tower_of_hanoi(start, empty, n - 1, answer)
        answer.append([start, end])
        tower_of_hanoi(empty, end, n - 1, answer)
    return answer


def solution(n):
    answer = []
    answer = tower_of_hanoi(1, 3, n, answer)
    return answer
