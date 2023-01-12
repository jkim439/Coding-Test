class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def search(self, key):
        node = self.head

        while node:
            if node.value[0] == key:
                return node.value[1]
            else:
                node = node.next

    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head

        else:
            node = self.head

            while node.next:
                node = node.next

            new = Node(value)
            new.prev = node
            node.next = new
            self.tail = new

    def remove(self, value):
        node = self.head

        if value == node.value:
            self.head = node.next
            self.head.prev = None
            del node

        else:
            while node.next:
                if node.next.value == value:
                    temp = node.next
                    if node.next.next:
                        node.next.next.prev = node
                        node.next = node.next.next
                    else:
                        node.next = None
                        self.tail = node
                    del temp

                else:
                    node = node.next


# Closed Addressing, Open Hashing, Chaining

buckets = [None] * 10


def get_key(data):
    return hash(data)


def hash_function(key):
    return key % 10


def save(data, value):
    key = get_key(data)
    index = hash_function(key)
    print(data, key, index)

    if buckets[index] is None:
        buckets[index] = DoublyLinkedList()
    buckets[index].insert([key, value])


def load(data):
    key = get_key(data)
    index = hash_function(key)

    if buckets[index] is not None:
        return buckets[index].search(key)
    else:
        return None


save("ab", 12)
save("ac", 34)
save("ad", 56)
save("ae", 78)
save("af", 90)
print(buckets)
print(load("ae"))
