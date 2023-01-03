# 베스트앨범
def solution(genres, plays):
    list = []
    dict = {}
    answer = []

    for i in range(len(genres)):
        list.append([i, genres[i], plays[i]])
        if genres[i] not in dict:
            dict[genres[i]] = plays[i]
        else:
            dict[genres[i]] += plays[i]

    dict = sorted(dict.items(), key=lambda item: item[1], reverse=True)
    list = sorted(list, key=lambda item: item[2], reverse=True)

    for i in range(len(dict)):
        k = 0
        for j in range(len(list)):
            if k > 1:
                break
            if list[j][1] == dict[i][0]:
                answer.append(list[j][0])
                k += 1

    return answer
