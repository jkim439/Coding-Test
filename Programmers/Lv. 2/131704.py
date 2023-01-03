# 택배상자
def solution(order):
    a = 1
    b = 0
    temp = []

    while a < len(order) + 1:
        temp.append(a)

        while temp[-1] == order[b]:
            b += 1
            temp.pop()

            if len(temp) == 0:
                break

        a += 1

    return b
