# 이진 변환 반복하기
def solution(s):
    a = 0
    b = 0
    while 1:
        if s == "1":
            return [a, b]
        a += 1
        b += len([c for c in s if c == "0"])
        s = str(bin(len([c for c in s if c == "1"]))[2:])
