# 길 찾기 게임
import sys

sys.setrecursionlimit(10000)


class Node:
    def __init__(self, n, x):
        self.n = n
        self.x = x
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, n, x):
        if self.root is None:
            self.root = Node(n, x)

        else:
            node = self.root

            while 1:
                if x < node.x:
                    if node.left is None:
                        node.left = Node(n, x)
                        break
                    else:
                        node = node.left

                elif node.x < x:
                    if node.right is None:
                        node.right = Node(n, x)
                        break
                    else:
                        node = node.right

    def preorder(self):
        def order(node):
            result.append(node.n)

            if node.left is not None:
                order(node.left)

            if node.right is not None:
                order(node.right)

        result = []
        order(self.root)
        return result

    def postorder(self):
        def order(node):
            if node.left is not None:
                order(node.left)

            if node.right is not None:
                order(node.right)

            result.append(node.n)

        result = []
        order(self.root)
        return result


def solution(nodeinfo):
    for i, n in enumerate(nodeinfo):
        n.append(i + 1)
    nodeinfo.sort(key=lambda x: -x[1])

    tree = Tree()
    for n in nodeinfo:
        tree.insert(n[2], n[0])

    return [tree.preorder(), tree.postorder()]
