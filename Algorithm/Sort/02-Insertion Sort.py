def insertion_sort(data):
    for turn in range(1, len(data)):
        for index in range(turn, 0, -1):
            if data[index - 1] > data[index]:
                data[index - 1], data[index] = data[index], data[index - 1]
            else:
                break
    return data


data = [7, 2, 4, 1, 6, 9, 3, 5, 8]
print(data)
insertion_sort(data)
print(data)
