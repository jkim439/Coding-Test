# [3차] 압축
def solution(msg):
    dic = {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
        "F": 6,
        "G": 7,
        "H": 8,
        "I": 9,
        "J": 10,
        "K": 11,
        "L": 12,
        "M": 13,
        "N": 14,
        "O": 15,
        "P": 16,
        "Q": 17,
        "R": 18,
        "S": 19,
        "T": 20,
        "U": 21,
        "V": 22,
        "W": 23,
        "X": 24,
        "Y": 25,
        "Z": 26,
    }

    answer = []
    i = 0
    msg += "*"

    while i < len(msg):
        temp = msg[i]
        if temp == "*":
            break

        j = i
        while temp in dic:
            j += 1
            if j >= len(msg):
                break
            temp += msg[j]

        if len(temp) > 1:
            in_dic = temp[:-1]
        else:
            in_dic = temp
        answer.append(dic[in_dic])

        add_dic = temp
        if add_dic not in dic:
            dic[add_dic] = len(dic) + 1

        i += len(in_dic)

    return answer
