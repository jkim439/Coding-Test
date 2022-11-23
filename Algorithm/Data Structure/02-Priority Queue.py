import queue

queue = queue.PriorityQueue()

queue.put((2, "Samsung"))
queue.put((1, "Hyundai"))

print(queue.qsize())

print(queue.get())
print(queue.get()[1])

print(queue.qsize())
