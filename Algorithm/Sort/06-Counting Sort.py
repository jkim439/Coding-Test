def counting_sort(data):
    count = [0] * (max(data) + 1)
    sorted = []

    for i in data:
        count[i] += 1

    for i in range(max(data) + 1):
        for _ in range(count[i]):
            sorted.append(i)

    return sorted


print(counting_sort([15, 27, 64, 25, 50, 17, 39, 28]))
