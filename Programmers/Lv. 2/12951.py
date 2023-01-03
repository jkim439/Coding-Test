# JadenCase 문자열 만들기
def solution(s):
    return " ".join(list(map(lambda x: x.capitalize(), s.split(" "))))
