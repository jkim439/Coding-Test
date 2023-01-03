class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class NodeManage:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head

    def show(self):
        node = self.head

        while node:
            print(node.value)
            node = node.next

    def insert(self, value):
        node = self.head

        while node.next:
            node = node.next

        new = Node(value)
        new.prev = node
        node.next = new
        self.tail = new

    def insert_before(self, value, before_value):
        node = self.head

        while node.next:
            if node.next.value == before_value:
                break
            else:
                node = node.next

        new = Node(value)
        new.prev = node
        new.next = node.next
        node.next.prev = new
        node.next = new

    def remove(self, value):
        node = self.head

        if value == node.value:
            self.head = node.next
            del node

        else:
            while node.next:
                if node.next.value == value:
                    temp = node.next
                    if node.next.next:
                        node.next = node.next.next
                    else:
                        node.next = None
                        self.tail = node
                    del temp

                else:
                    node = node.next


linkedlist = NodeManage("a")
linkedlist.show()
print("---")
linkedlist.insert("b")
linkedlist.insert("d")
linkedlist.insert("e")
linkedlist.insert_before("c", "d")
linkedlist.show()
print("---")
linkedlist.remove("e")
linkedlist.show()
