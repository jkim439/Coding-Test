class Node:
    def __init__(self, key):
        self.key = key
        self.child = dict()


class Trie:
    def __init__(self):
        self.root = Node(None)

    def insert(self, value):
        node = self.root

        for v in value:
            if v not in node.child:
                node.child[v] = Node(v)
            node = node.child[v]

        node.key = value

    def search(self, value):
        node = self.root

        for v in value:
            if v in node.child:
                node = node.child[v]
            else:
                return False
        return node.key


trie = Trie()
trie.insert("C")
trie.insert("CAT")
print(trie.search("CAT"))
