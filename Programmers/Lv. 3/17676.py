# [1차] 추석 트래픽
def convert(s):
    end = (
        (int(s[11:13]) * 3600 * 1000)
        + (int(s[14:16]) * 60 * 1000)
        + (int(float(s[17:23]) * 1000))
    )
    start = end - int(float(s[24:-1]) * 1000) + 1

    return [start, end]


def solution(lines):
    answer = 0

    times = []
    for l in lines:
        times.append(convert(l))

    for t in times:
        start = [t[0], t[0] + 999]
        start_window = [
            i for i, v in enumerate(times) if v[0] <= start[1] and start[0] <= v[1]
        ]

        end = [t[1], t[1] + 999]
        end_window = [
            i for i, v in enumerate(times) if v[0] <= end[1] and end[0] <= v[1]
        ]

        answer = max(answer, len(start_window), len(end_window))

    return answer
