# 기둥과 보 설치
def check_pillar(x, y, answer):
    if (
        y == 0
        or [x - 1, y, 1] in answer
        or [x, y, 1] in answer
        or [x, y - 1, 0] in answer
    ):
        return True
    else:
        return False


def check_beam(x, y, answer):
    if (
        [x, y - 1, 0] in answer
        or [x + 1, y - 1, 0] in answer
        or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer)
    ):
        return True
    else:
        return False


def check_whole(x, y, a, answer):
    temp = [x, y, a]
    answer.remove(temp)
    for x, y, a in answer:
        if a == 0:
            if check_pillar(x, y, answer) is False:
                answer.append(temp)
                return
        if a == 1:
            if check_beam(x, y, answer) is False:
                answer.append(temp)
                return


def solution(n, build_frame):
    answer = []
    for x, y, a, b in build_frame:
        if b == 1:
            if a == 0:
                if check_pillar(x, y, answer) is True:
                    answer.append([x, y, a])
            else:
                if check_beam(x, y, answer) is True:
                    answer.append([x, y, a])
        else:
            check_whole(x, y, a, answer)
    return sorted(answer, key=lambda x: (x[0], x[1], x[2]))
