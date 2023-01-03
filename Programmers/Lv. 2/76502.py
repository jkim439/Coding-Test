# 괄호 회전하기
def rotate(s):
    stack = []
    for c in s:
        if len(stack) == 0:
            stack.append(c)
        else:
            if c == ")" and stack[-1] == "(":
                stack.pop()
            elif c == "]" and stack[-1] == "[":
                stack.pop()
            elif c == "}" and stack[-1] == "{":
                stack.pop()
            else:
                stack.append(c)

    return 1 if len(stack) == 0 else 0


def solution(s):
    n = 0
    n += rotate(s)

    x = 1
    while x < len(s):
        s_temp = s
        s = s_temp[1:]
        s += s_temp[0]
        n += rotate(s)
        x += 1

    return n


print(solution("[{]}"))
