class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

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

    def search(self, value):
        node = self.head

        while node:
            if node.value[0] == value:
                return node.value[1]
            else:
                node = node.next


# Plain Hash
# def hash_function(data):
#     return hash(data)


# djb2 Hash (38)
# def hash_function(data):
#     hash = 5381
#     for d in data:
#         hash = (((hash << 5) + hash) + ord(d)) & 0xFFFFFFFF
#     return hash


# FNV-1a Hash (12)
def hash_function(data):
    hash = 0x811C9DC5
    for d in data:
        hash = ((ord(d) ^ hash) * 0x01000193) & 0xFFFFFFFF
    return hash


def get_idx(key):
    return key % 10


def save(data, value):
    key = hash_function(data)
    index = get_idx(key)
    print(data, key, index)

    if buckets[index] is None:
        buckets[index] = DoublyLinkedList()
    buckets[index].insert([key, value])


def load(data):
    key = hash_function(data)
    index = get_idx(key)

    if buckets[index] is not None:
        return buckets[index].search(key)
    else:
        return None


buckets = [None] * 10
save("ab", 12)
save("ac", 34)
save("ad", 56)
save("ae", 78)
save("af", 90)
print(buckets)
print(load("ae"))
