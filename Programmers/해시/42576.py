# 완주하지 못한 선수
def solution(participant, completion):
    temp = 0
    dict = {}

    for name in participant:
        key = hash(name)
        temp += key
        dict[key] = name

    for name in completion:
        key = hash(name)
        temp -= key

    return dict[temp]
