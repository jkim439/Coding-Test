def sequential_search(list, value):
    for index in range(len(list)):
        if list[index] == value:
            return True
    return False


data = [7, 2, 4, 1, 6, 9, 3, 5, 8]
print(data)
print(sequential_search(data, 99))
