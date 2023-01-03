# 괄호 변환
def solution(p):
    global answer
    answer = ""

    def recursive(s):
        global answer

        if len(s) == 0:
            return
        u = s[0]
        v = ""
        for i in range(1, len(s)):
            if u.count("(") != u.count(")"):
                u += s[i]
            else:
                v = s[i:]
                break

        u_correct = True
        u_point = 0

        for u_char in u:
            if u_char == "(":
                u_point += 1
            else:
                u_point -= 1
            if u_point < 0:
                u_correct = False
                break

        if u_correct is True:
            answer += u
            recursive(v)

        else:

            u = u[1:-1]
            u = u.replace("(", "*")
            u = u.replace(")", "(")
            u = u.replace("*", ")")

            answer += "("
            recursive(v)
            answer += ")" + u

    recursive(p)
    return answer
