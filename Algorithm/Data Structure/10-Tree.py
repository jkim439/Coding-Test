class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class NodeManage:
    def __init__(self, value):
        self.root = Node(value)

    def insert(self, value):
        node = self.root

        while True:
            if value < node.value:
                if node.left is None:
                    node.left = Node(value)
                    break
                else:
                    node = node.left
            else:
                if node.right is None:
                    node.right = Node(value)
                    break
                else:
                    node = node.right

    def search(self, value):
        node = self.root

        while True:
            if value == node.value:
                return True

            elif value < node.value:
                if node.left is None:
                    return False
                else:
                    node = node.left

            else:
                if node.right is None:
                    return False
                else:
                    node = node.right


bst = NodeManage(5)
bst.insert(3)
bst.insert(1)
bst.insert(9)
print(bst.search(1))
