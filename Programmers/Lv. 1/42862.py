# 체육복
def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    while reserve:
        pop = reserve.pop(0)
        if pop - 1 in lost and pop not in lost and pop - 1 not in reserve:
            lost.remove(pop - 1)
            continue
        if pop + 1 in lost and pop not in lost and pop + 1 not in reserve:
            lost.remove(pop + 1)
            continue
        if pop in lost:
            lost.remove(pop)
    return n - len(lost)
