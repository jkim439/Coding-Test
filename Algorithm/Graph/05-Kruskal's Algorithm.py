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
    ["A", "B", 7],
    ["A", "D", 5],
    ["B", "A", 7],
    ["B", "C", 8],
    ["B", "D", 9],
    ["B", "E", 7],
    ["C", "B", 8],
    ["C", "E", 5],
    ["D", "A", 5],
    ["D", "B", 9],
    ["D", "E", 7],
    ["D", "F", 6],
    ["E", "B", 7],
    ["E", "C", 5],
    ["E", "D", 7],
    ["E", "F", 8],
    ["E", "G", 9],
    ["F", "D", 6],
    ["F", "E", 8],
    ["F", "G", 11],
    ["G", "E", 9],
    ["G", "F", 11],
]

print(kruskal(graph))
