# 뉴스 클러스터링
from collections import Counter


def solution(str1, str2):

    s1, s2 = [], []
    for i in range(len(str1) - 1):
        if str1[i].isalpha() is True and str1[i + 1].isalpha() is True:
            s1.append(str1[i].lower() + str1[i + 1].lower())
    for i in range(len(str2) - 1):
        if str2[i].isalpha() is True and str2[i + 1].isalpha() is True:
            s2.append(str2[i].lower() + str2[i + 1].lower())

    s1 = Counter(s1)
    s2 = Counter(s2)
    s1ns2 = s1 & s2
    s1us2 = s1 | s2

    try:
        return int(len(list(s1ns2.elements())) / len(list(s1us2.elements())) * 65536)
    except:
        return 65536
