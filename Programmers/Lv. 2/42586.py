# 기능개발
def solution(progresses, speeds):
    answer = []
    index = 0

    while index < len(progresses):
        distribute = 0
        for i in range(index, len(progresses)):
            progresses[i] += speeds[i]
        if progresses[index] >= 100:
            for j in range(index, len(progresses)):
                if progresses[j] >= 100:
                    distribute += 1
                    index += 1
                else:
                    break
            answer.append(distribute)
    return answer
