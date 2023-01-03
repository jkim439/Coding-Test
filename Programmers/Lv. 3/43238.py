# 입국심사
def solution(n, times):
    left = 1
    right = max(times) * n

    while left < right:
        people = 0
        middle = (left + right) // 2

        for time in times:
            people += middle // time

        if n <= people:
            right = middle
        else:
            left = middle + 1

    return left
