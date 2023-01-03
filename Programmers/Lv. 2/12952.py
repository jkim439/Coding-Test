# N-Queen
def n_queen(r, n, queen):
    count = 0

    if n == r:
        return 1

    for c in range(n):
        queen[r] = c

        for r0 in range(r):
            if queen[r] == queen[r0] or abs(r - r0) == abs(queen[r] - queen[r0]):
                break
        else:
            count += n_queen(r + 1, n, queen)

    return count


def solution(n):
    return n_queen(0, n, [0] * n)
