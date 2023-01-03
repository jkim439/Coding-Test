# 할인 행사
def solution(want, number, discount):
    answer = []

    for d in range(len(discount) - 9):
        result = True
        dis = discount[d : d + 10]
        for w, n in zip(want, number):
            if dis.count(w) < n:
                result = False
                break
        if result is True:
            answer.append(d)

    return len(answer)
