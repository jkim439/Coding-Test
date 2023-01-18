# 기지국 설치
from math import ceil


def solution(n, stations, w):
    apt = []
    apt.append(stations[0] - 1 - w)
    for i in range(1, len(stations)):
        apt.append((stations[i] - 1 - w - 1) - (stations[i - 1] - 1 + w))
    apt.append(n - 1 - (stations[-1] - 1 + w))

    answer = 0
    for a in apt:
        answer += ceil(a / (2 * w + 1))

    return answer
