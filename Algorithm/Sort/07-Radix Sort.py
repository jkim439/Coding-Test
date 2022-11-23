def radix_sort(data):
    buckets = [[] for _ in range(10)]
    queue = data
    ten = 1

    while ten < max(data):
        while queue:
            n = queue.pop(0)
            buckets[(n // ten) % 10].append(n)

        for bucket in buckets:
            while bucket:
                queue.append(bucket.pop(0))

        ten *= 10

    return queue


print(radix_sort([15, 27, 64, 25, 50, 17, 39, 28]))
