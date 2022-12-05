parent, rank = {}, {}


def kruskal(graph):
    mst = []

    for node in set([item[0] for item in graph]):
        parent[node] = node
        rank[node] = 0

    for edge in sorted(graph, key=lambda x: x[2]):
        node1, node2, _ = edge
        if find(node1) != find(node2):
            union(node1, node2)
            mst.append(edge)

    return mst


def find(node):
    # path-compression
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(node1, node2):
    root1, root2 = find(node1), find(node2)

    # union-by-rank
    if rank[root1] < rank[root2]:
        parent[root1] = root2
    elif rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        rank[root2] += 1
        parent[root1] = root2


graph = [
    [1, 2, 7],
    [1, 4, 5],
    [2, 1, 7],
    [2, 3, 8],
    [2, 4, 9],
    [2, 5, 7],
    [3, 2, 8],
    [3, 5, 5],
    [4, 1, 5],
    [4, 2, 9],
    [4, 5, 7],
    [4, 6, 6],
    [5, 2, 7],
    [5, 3, 5],
    [5, 4, 7],
    [5, 6, 8],
    [5, 7, 9],
    [6, 4, 6],
    [6, 5, 8],
    [6, 7, 11],
    [7, 5, 9],
    [7, 6, 11],
]

print(kruskal(graph))
