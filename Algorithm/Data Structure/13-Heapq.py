from heapq import *

heap = [42, 67, 32, 91, 12, 45, 76]
heapify(heap)
heappush(heap, 11)
print(heap, heappop(heap))

max = nlargest(len(heap), heap)[0]
print(max)

heap = nlargest(len(heap), heap)[1:]
heapify(heap)
print(heap)
