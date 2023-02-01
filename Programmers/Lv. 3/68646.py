# 풍선 터트리기
def solution(a):
    answer = 2

    left = [a[0]]
    right = [a[-1]]

    for i in range(1, len(a)):
        left.append(min(left[-1], a[i]))
        right.append(min(right[-1], a[len(a) - 1 - i]))

    for i in range(1, len(a) - 1):
        if a[i] < left[i - 1] or a[i] < right[len(a) - 2 - i]:
            answer += 1

    return answer
