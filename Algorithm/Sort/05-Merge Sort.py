def merge_sort(data):
    if len(data) <= 1:
        return data
    else:
        median = len(data) // 2
        left = merge_sort(data[:median])
        right = merge_sort(data[median:])

        merged = []
        l = r = 0

        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                merged.append(left[l])
                l += 1
            else:
                merged.append(right[r])
                r += 1

        while l < len(left):
            merged.append(left[l])
            l += 1

        while r < len(right):
            merged.append(right[r])
            r += 1

        return merged


data = [7, 2, 4, 1, 6, 9, 3, 5, 8]
print(data)
print(merge_sort(data))
