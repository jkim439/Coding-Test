def search(data, value):
    if data[0] == value:
        return True

    if len(data) <= 1:
        return False

    median = len(data) // 2
    if value == data[median]:
        return True
    elif value < data[median]:
        return search(data[:median], value)
    else:
        return search(data[median:], value)


data = [11, 21, 36, 47, 68, 93]
print(data)
print(search(data, 21))
