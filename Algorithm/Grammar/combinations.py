from itertools import combinations

data = ["1", "2", "3", "4", "5"]
list = list(combinations(data, 2))
print(list)

list = [item for sublist in list for item in sublist]
print(list)


list2 = [item for sublist in list for item in sublist]
