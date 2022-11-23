from itertools import accumulate


def prefix_sum(data):
    for item in accumulate(data):
        print(item)


prefix_sum([1, 2, 3, 4, 5])


from operator import *


def prefix_mul(data):
    for item in accumulate(data, mul):
        print(item)


prefix_mul([1, 2, 3, 4, 5])
