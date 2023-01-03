# k진수에서 소수 개수 구하기
def convert(n, base):
    if n == 0:
        return "0"
    numbers = "0123456789ABCDEF"
    result = ""
    while n > 0:
        n, mod = divmod(n, base)
        result += numbers[mod]
    return result[::-1]


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    based = list(convert(n, k))

    i = 0
    while i < len(based):
        t = ""
        if based[i] == "0":
            i += 1
        else:
            while i < len(based) and based[i] != "0":
                t += based[i]
                i += 1
            if is_prime(int(t)) is True:
                answer += 1
    return answer
