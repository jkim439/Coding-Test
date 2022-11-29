# [3차] 파일명 정렬
def solution(files):
    answer = []
    names = []

    for idx, file in enumerate(files):
        head, number, tail = "", "", ""
        step = 0

        for i in range(len(file)):
            if step == 0:
                if file[i].isdecimal() is False:
                    head += str(file[i])
                else:
                    number += str(file[i])
                    step = 1
            elif step == 1:
                if len(number) >= 5:
                    break
                if file[i].isdecimal() is True:
                    number += str(file[i])
                else:
                    break

        head = head.lower()
        number = (str(0) * (5 - len(number))) + number
        tail = file[len(head) + len(number) :].lower()

        names.append([idx, head, number, tail])

    names.sort(key=lambda x: (x[1], x[2]))
    while names:
        name = names.pop(0)
        if names:
            temp = [name[0]]
            while len(names) > 0 and name[1] == names[0][1] and name[2] == names[0][2]:
                temp.append(names[0][0])
                names.pop(0)
            temp.sort()
            answer += temp
        else:
            answer += [name[0]]
    return [files[i] for i in answer]
