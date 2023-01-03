# 위장
def solution(clothes):
    answer = 1
    dict = {}

    for cloth in clothes:
        type = cloth[1]
        if type in dict:
            dict[type] += 1
        else:
            dict[type] = 2

    for value in dict.values():
        answer *= value

    return answer - 1
