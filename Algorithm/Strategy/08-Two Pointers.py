def two_pointers(data, k):
    data.sort()
    l = 0
    r = len(data) - 1

    while l <= r:
        if data[l] + data[r] < k:
            l += 1
        elif data[l] + data[r] > k:
            r -= 1
        else:
            print(data[l], "+", data[r])
            l += 1
            r -= 1


two_pointers([3, 9, 25, 22, 1, 6, 5, 11, 19, 28, 17, 12, 16], 27)
