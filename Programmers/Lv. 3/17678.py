# [1차] 셔틀버스
def solution(n, t, m, timetable):
    answer = 0
    crew = [int(time[:2]) * 60 + int(time[3:]) for time in timetable]
    crew.sort()
    bus = [540 + t * i for i in range(n)]

    i = 0
    for b in bus:
        count = 0
        while count < m and i < len(crew) and crew[i] <= b:
            i += 1
            count += 1
        if count < m:
            answer = b
        else:
            answer = crew[i - 1] - 1

    return str(answer // 60).zfill(2) + ":" + str(answer % 60).zfill(2)
