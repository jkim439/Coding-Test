def sliding_window(data, k):
    answer = window = sum(data[:k])

    for i in range(k, len(data)):
        window += data[i] - data[i - k]
        answer = max(answer, window)
    return answer


print(sliding_window([3, -1, 8, -2, 0, 9, -3], 3))
