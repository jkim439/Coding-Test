# 2개 이하로 다른 비트
def solution(numbers):
    answer = []

    for number in numbers:
        if number % 2 == 0:
            answer.append(number + 1)
        else:
            n = "0" + bin(number)[2:]
            i = n.rfind("0")
            n = list(n)
            n[i] = "1"
            n[i + 1] = "0"
            answer.append(int("".join(n), 2))

    return answer
