# 이중우선순위큐
import heapq


def solution(operations):
    answer = [0, 0]
    heap = []
    while operations:
        operation = operations.pop(0)
        if operation[0] == "I":
            heapq.heappush(heap, int(operation[2:]))
        if operation == "D 1" and heap:
            heapq.heapify(heapq.nlargest(len(heap), heap)[1:])
        if operation == "D -1" and heap:
            heapq.heappop(heap)
    if len(heap) > 0:
        answer = [heapq.nlargest(len(heap), heap)[0], heap[0]]
    return answer
