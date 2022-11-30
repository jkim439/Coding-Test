# 방문 길이
def solution(dirs):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    y, x = [0, 0]
    visited = []

    for dir in dirs:
        if dir == "D":
            i = 0
        elif dir == "R":
            i = 1
        elif dir == "U":
            i = 2
        else:
            i = 3

        ny, nx = [y + dy[i], x + dx[i]]

        if -5 <= ny <= 5 and -5 <= nx <= 5:
            path = [y, x, ny, nx]
            path_reversed = path[2:4] + path[0:2]

            if path not in visited and path_reversed not in visited:
                visited.append(path)

            y, x = [ny, nx]

    return len(visited)
