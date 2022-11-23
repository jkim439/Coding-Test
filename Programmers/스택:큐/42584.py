# 주식가격
from collections import deque


def solution(prices):
    answer = []
    d_prices = deque(prices)

    while len(d_prices) != 0:
        count = 0
        first = d_prices.popleft()

        for p in d_prices:
            count += 1
            if p < first:
                break
        answer.append(count)

    return answer
