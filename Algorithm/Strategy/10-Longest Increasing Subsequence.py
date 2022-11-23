from bisect import bisect_left


def lis(data):
    dp = [1]
    array = [data[0]]

    for i in range(1, len(data)):
        if array[-1] < data[i]:
            dp.append(dp[-1] + 1)
            array.append(data[i])
        else:
            array[bisect_left(array, data[i])] = data[i]

    return array


print(lis([5, 2, 1, 4, 3, 5]))
