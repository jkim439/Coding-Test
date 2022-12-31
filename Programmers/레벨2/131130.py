# 혼자 놀기의 달인
def solution(cards):
    count = []
    queue = [i - 1 for i in cards]
    visited = []

    for q in queue:
        if q in visited:
            continue
        temp = []
        temp.append(q)
        i = queue[q]

        while queue[i] not in temp:
            temp.append(i)
            i = queue[i]

        temp.append(i)
        temp = set(temp)
        count.append(len(temp))
        visited.extend(temp)

    count.sort(reverse=True)
    if len(count) > 1:
        return count[0] * count[1]
    else:
        return 0
