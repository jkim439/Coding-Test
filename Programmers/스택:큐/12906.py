# 같은 숫자는 싫어
def solution(arr):
    answer = [arr[0]]
    for index in range(1, len(arr)):
        if answer[-1] != arr[index]:
            answer.append(arr[index])
    return answer
