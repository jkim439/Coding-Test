# 두 큐 합 같게 만들기
from collections import deque


def solution(queue1, queue2):
    deque1, deque2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(deque1), sum(deque2)
    for i in range(300000):
        if sum1 == sum2:
            return i
        elif sum1 > sum2:
            num = deque1.popleft()
            deque2.append(num)
            sum1 -= num
            sum2 += num
        else:
            num = deque2.popleft()
            deque1.append(num)
            sum2 -= num
            sum1 += num
    return -1
