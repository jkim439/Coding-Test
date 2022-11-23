# 다음 큰 숫자
def solution(n):
    n_bin = bin(n).count("1")
    n_next = n
    while 1:
        n_next += 1
        n_next_bin = bin(n_next).count("1")
        if n_bin == n_next_bin:
            return n_next
