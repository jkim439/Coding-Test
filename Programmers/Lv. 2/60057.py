# 문자열 압축
def solution(s):
    answer = len(s)

    for i in range(1, len(s)):
        temp = ""
        ss = []
        j = 0

        while j < len(s):
            ss.append(s[j : j + i])
            j += i

        while ss:
            ss0 = ss.pop(0)
            n = 1
            while ss and ss0 == ss[0]:
                n += 1
                ss.pop(0)
            if n == 1:
                temp += ss0
            else:
                temp += str(n) + ss0
        answer = min(answer, len(temp))
    return answer
