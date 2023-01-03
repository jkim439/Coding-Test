# 삼각 달팽이
def solution(n):
    box = [[] for _ in range(n + 1)]
    for r in range(1, n + 1):
        box[r] = [None for _ in range(r)]

    r_s = 1
    r_e = n
    c_s = 0
    c_e = -1
    i = 1

    while r_s <= r_e:
        for r in range(r_s, r_e):
            box[r][c_s] = i
            i += 1
        for c in range(r_e):
            if box[r_e][c] is None:
                box[r_e][c] = i
                i += 1
        for r in range(r_e - 1, r_s, -1):
            box[r][c_e] = i
            i += 1

        r_s += 2
        r_e -= 1
        c_s += 1
        c_e -= 1

    return [i for sublist in box[1:] for i in sublist]
