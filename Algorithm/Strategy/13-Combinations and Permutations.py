def combinations(m, data, comb, depth):
    if len(comb) == m:
        print(comb)
        return

    if len(data) == depth:
        return

    comb.append(data[depth])
    combinations(m, data, comb, depth + 1)

    comb.pop()
    combinations(m, data, comb, depth + 1)


combinations(2, [1, 2, 3, 4], list(), 0)


def permutations(m, data, perm, visited):
    if len(perm) == m:
        print(perm)
        return

    if len(visited) == 0:
        visited = [0] * len(data)

    for i, v in enumerate(data):
        if visited[i] == 0:
            visited[i] = 1

            perm.append(v)
            permutations(m, data, perm, visited)
            perm.pop()

            visited[i] = 0


permutations(3, [1, 2, 3, 4], list(), list())
