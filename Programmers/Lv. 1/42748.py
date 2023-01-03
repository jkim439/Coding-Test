# K번째수
def solution(array, commands):
    answer = []
    for index in range(len(commands)):
        answer.append(
            sorted(array[commands[index][0] - 1 : commands[index][1]])[
                commands[index][2] - 1
            ]
        )
    return answer
