# [3차] n진수 게임
def convert(n, base):
    if n == 0:
        return "0"
    numbers = "0123456789ABCDEF"
    result = ""
    while n > 0:
        n, mod = divmod(n, base)
        result += numbers[mod]
    return result[::-1]


def solution(n, t, m, p):
    data = ""
    for i in range(t * m):
        data += convert(i, n)

    answer = ""
    i = p - 1
    while len(answer) < t:
        answer += data[i]
        i += m

    return answer
