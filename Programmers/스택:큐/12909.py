# 올바른 괄호
def solution(s):
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return stack == []
