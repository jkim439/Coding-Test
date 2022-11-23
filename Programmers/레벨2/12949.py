# 행렬의 곱셈
def solution(arr1, arr2):
    r = len(arr1)
    c = len(arr2[0])
    answer = [[0] * c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            for k in range(len(arr2)):
                answer[i][j] = answer[i][j] + (arr1[i][k] * arr2[k][j])

    return answer
