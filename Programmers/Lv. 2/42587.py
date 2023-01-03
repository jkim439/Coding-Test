# 프린터
def solution(priorities, location):
    answer = 1
    while True:
        first = priorities[0]
        if any(i > first for i in priorities) is True:
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
            priorities.append(priorities.pop(0))
        else:
            if location == 0:
                return answer
            else:
                priorities.pop(0)
                location -= 1
                answer += 1
