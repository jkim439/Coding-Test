# 여행경로
def solution(tickets):
    tickets.sort(reverse=True)
    routes = dict()
    for origin, destination in tickets:
        if origin in routes:
            routes[origin].append(destination)
        else:
            routes[origin] = [destination]
    answer = []
    stack = ["ICN"]

    while stack:
        top = stack[-1]
        if top not in routes or len(routes[top]) == 0:
            answer.append(stack.pop())
        else:
            stack.append(routes[top].pop())
    answer.reverse()
    return answer
