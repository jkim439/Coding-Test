import copy

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
a[1].append(5)
print(a)  # [[1, 2], [3, 4, 5]]
print(b)  # [[1, 2], [3, 4]]
