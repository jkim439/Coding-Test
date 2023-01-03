# Open Addressing, Closed Hashing

buckets = [None] * 10


def get_key(data):
    return hash(data[0])


def hash_function(key):
    return key % 10


def save(data, value):
    key = get_key(data)
    index = hash_function(key)

    if buckets[index] is None:
        buckets[index] = [key, value]
    else:
        for i in range(index, len(buckets)):
            if buckets[i] is None:
                buckets[i] = [key, value]
                return


def load(data):
    key = get_key(data)
    index = hash_function(key)

    for i in range(index, len(buckets)):
        if buckets[i] is not None:
            if buckets[i][0] == key:
                return buckets[i][1]
    return None


print(buckets)

save("a", 12)
save("c", 34)
save("e", 343)
save("g", 78)
save("i", 90)

print(buckets)
print(load("e"))
