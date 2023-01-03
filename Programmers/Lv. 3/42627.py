# 디스크 컨트롤러
import heapq


def solution(jobs):
    answer, i, now, start = 0, 0, 0, -1
    heap = []
    while i < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(heap, [job[1], job[0]])
        if len(heap) > 0:
            job = heapq.heappop(heap)
            i += 1
            start = now
            now += job[0]
            answer += now - job[1]
        else:
            now += 1
    return answer // len(jobs)
