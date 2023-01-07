def bubble_sort(data):
    for turn in range(1, len(data)):
        swap = False
        for index in range(len(data) - turn):
            if data[index] > data[index + 1]:
                data[index], data[index + 1] = data[index + 1], data[index]
                swap = True
        if not swap:
            break
    return data


data = [7, 2, 4, 1, 6, 9, 3, 5, 8]
print(data)
bubble_sort(data)
print(data)
