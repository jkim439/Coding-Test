# 타겟 넘버
def solution(numbers, target):
    answer = 0
    stack = [[numbers[0], 0], [-1 * numbers[0], 0]]

    while stack:
        number, index = stack.pop()
        index += 1

        if index < len(numbers):
            stack.append([number + numbers[index], index])
            stack.append([number - numbers[index], index])
        else:
            if number == target:
                answer += 1
    return answer
