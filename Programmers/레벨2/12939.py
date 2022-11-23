# 최댓값과 최솟값
def solution(s):
    s = list(map(int, s.split(" ")))
    return str(min(s)) + " " + str(max(s))
