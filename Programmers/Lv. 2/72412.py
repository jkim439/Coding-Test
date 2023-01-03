# 순위 검색
from bisect import bisect_left
from collections import defaultdict
from itertools import combinations


def solution(information, queries):
    answer = []
    comb = []
    hash = defaultdict(list)

    for i in range(5):
        for c in list(combinations([0, 1, 2, 3], i)):
            comb.append(c)

    for info in information:
        info = info.split()
        k = info[:-1]
        v = int(info[-1])
        for c in comb:
            temp = k.copy()
            for i in c:
                temp[i] = "-"
            key = "".join(temp)
            hash[key].append(v)

    for value in hash.values():
        value.sort()

    for query in queries:
        query = query.replace("and ", "").split()
        key = "".join(query[:-1])
        value = int(query[-1])
        count = 0
        if key in hash:
            i = bisect_left(hash[key], value)
            count = len(hash[key]) - i
        answer.append(count)

    return answer
