# 가장 긴 팰린드롬
def solution(s):
    answer = 0

    for i in range(len(s)):
        for j in range(len(s) - 1, 0, -1):
            if s[i:j] == s[j:i:-1]:
                answer = max(answer, len(s[i:j]))
    return answer + 1
