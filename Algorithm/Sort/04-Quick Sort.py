def quick_sort(data):
    if len(data) <= 1:
        return data
    else:
        pivot = data[0]
        left = [item for item in data[1:] if item < pivot]
        right = [item for item in data[1:] if pivot < item]
        return quick_sort(left) + [pivot] + quick_sort(right)


data = [7, 2, 4, 1, 6, 9, 3, 5, 8]
print(data)
print(quick_sort(data))
