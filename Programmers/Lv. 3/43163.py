# 단어 변환
def solution(begin, target, words):
    if target not in words:
        return 0

    answer = 0
    stack = [begin]
    visited = [0 for i in words]

    while stack:
        print(stack)
        node = stack.pop()

        if node == target:
            return answer

        answer += 1
        for i in range(len(words)):
            dif = 0
            for j in range(len(node)):
                if node[j] != words[i][j]:
                    dif += 1
            if dif == 1:
                if visited[i] == 1:
                    continue
                else:
                    visited[i] = 1
                    stack.append(words[i])

    return answer
