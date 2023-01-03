# 야간 전술보행
def solution(distance, scope, times):
    answer = distance
    for i, s in enumerate(scope):
        start, end = sorted(s)
        for time in range(start, end + 1):
            if 0 < time % (times[i][0] + times[i][1]) <= times[i][0]:
                answer = min(answer, time)
    return answer
