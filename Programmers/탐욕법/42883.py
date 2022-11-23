# 큰 수 만들기
def solution(number, k):
    stack = []
    for num in number:
        while stack and int(stack[-1]) < int(num) and k > 0:
            stack.pop()
            k -= 1
        stack.append(str(num))
    return "".join(stack[: len(number) - k])
