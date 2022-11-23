# 최소직사각형
def solution(sizes):
    large = []
    small = []
    for n1, n2 in sizes:
        if n1 > n2:
            large.append(n1)
            small.append(n2)
        else:
            large.append(n2)
            small.append(n1)
    answer = max(large) * max(small)
    return answer
