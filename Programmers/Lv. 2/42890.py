# 후보키
from itertools import combinations


def solution(relation):
    answer = []

    for n in range(1, len(relation[0]) + 1):
        indexes = list(combinations(range(0, len(relation[0])), n))

        for index in indexes:
            unique = True

            s = ""
            for i in index:
                s += relation[0][i]
            temp = [s]

            for r in range(1, len(relation)):
                s = ""
                for i in index:
                    s += relation[r][i]
                if s not in temp:
                    temp.append(s)

            if len(relation) == len(temp):
                index = list(map(str, index))
                s = "".join(index)

                for a in answer:
                    if (len(set(a) & set(s))) == len(a):
                        unique = False
                        break

                if unique is True:
                    answer.append(s)

    return len(answer)
