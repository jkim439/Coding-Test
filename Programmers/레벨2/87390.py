# n^2 배열 자르기
def solution(n, left, right):
    answer = []

    for i in range((left // n) + 1, (right // n) + 2):
        if i == 1:
            answer.extend([i for i in range(1, n + 1)])
        elif 1 < i < n:
            for _ in range(i):
                answer.append(i)
            answer.extend([i for i in range(i + 1, n + 1)])
        else:
            answer.extend([n] * n)

    return answer[left - n * (left // n) : (right - n * (left // n)) + 1]
