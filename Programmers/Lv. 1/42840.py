# 모의고사
def solution(answers):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = [0 for i in range(3)]

    for i, answer in enumerate(answers):
        if answer == a[i % len(a)]:
            scores[0] += 1
        if answer == b[i % len(b)]:
            scores[1] += 1
        if answer == c[i % len(c)]:
            scores[2] += 1

    answer = []
    for i, score in enumerate(scores):
        if score == max(scores):
            answer.append(i + 1)

    return answer
