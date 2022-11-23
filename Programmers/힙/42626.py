# 더 맵게
import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while any(i <= K for i in scoville):
        if len(scoville) <= 1:
            return -1
        scoville.append(heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))
        answer += 1
    return answer
