# 테이블 해시 함수
def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key=lambda x: (x[col - 1], -x[0]))
    S = [sum([d % (i + 1) for d in data[i]]) for i in range(row_begin - 1, row_end)]

    for s in S:
        answer = answer ^ s

    return answer
