# H-Index
def solution(citations):
    citations = sorted(citations, reverse=True)
    for i, c in enumerate(citations):
        if i >= c:
            return i
    return len(citations)
