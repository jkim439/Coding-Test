from itertools import permutations

data = ["1", "2", "3", "4", "5"]
list = list(permutations(data, 2))
print(list)

list = [item for sublist in list for item in sublist]
print(list)
