# 카펫
def solution(brown, yellow):
    x = y = 3
    while True:
        if x * y == brown + yellow and (x - 2) * (y - 2) == yellow:
            return [x, y]
        else:
            if x > y:
                y += 1
                continue
            else:
                x += 1
                y = 3
                continue
