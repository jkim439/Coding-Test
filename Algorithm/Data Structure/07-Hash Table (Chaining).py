# Closed Addressing, Open Hashing, Chaining

buckets = [None] * 10


def get_key(data):
    return hash(data)


def hash_function(key):
    return key % 10


def save(data, value):
    key = get_key(data)
    index = hash_function(key)

    if buckets[index] is None:
        buckets[index] = [[key, value]]
    else:
        buckets[index].append([key, value])


def load(data):
    key = get_key(data)
    index = hash_function(key)

    for i in range(len(buckets[index])):
        if buckets[index][i][0] == key:
            return buckets[index][i][1]
    return None


print(buckets)

save("a", 12)
save("c", 34)
save("e", 123)
save("g", 78)
save("i", 90)

print(buckets)
print(load("e"))
