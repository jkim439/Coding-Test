# 연속 부분 수열 합의 개수
def solution(elements):
    answer = []
    element = elements + elements

    for i in range(1, len(elements) + 1):
        if i == 1:
            answer.extend(list(set(elements)))
        else:
            temp = []
            for j in range(len(elements)):
                temp.append(sum(element[j : j + i]))
            answer.extend(list(set(temp)))

    return len(set(answer))
