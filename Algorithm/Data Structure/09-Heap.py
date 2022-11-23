class Heap:
    def __init__(self, value):
        self.array = []
        self.array.append(None)
        self.array.append(value)

    def insert(self, value):
        self.array.append(value)
        idx = len(self.array) - 1

        while True:
            parent = idx // 2

            if idx <= 1:
                break

            else:
                if self.array[idx] > self.array[parent]:
                    self.array[idx], self.array[parent] = (
                        self.array[parent],
                        self.array[idx],
                    )
                    idx = parent
                else:
                    break

    def pop(self):
        print(self.array[1])
        self.array[1], self.array[-1] = self.array[-1], self.array[1]
        del self.array[-1]

        idx = 1

        while True:
            left = idx * 2
            right = left + 1

            if len(self.array) - 1 < left:
                break

            elif left < len(self.array) <= right:
                if self.array[idx] < self.array[left]:
                    self.array[idx], self.array[left] = (
                        self.array[left],
                        self.array[idx],
                    )
                    idx = left
                else:
                    break

            else:
                if self.array[left] < self.array[right]:
                    if self.array[idx] < self.array[right]:
                        self.array[idx], self.array[right] = (
                            self.array[right],
                            self.array[idx],
                        )
                        idx = right
                    else:
                        break
                else:
                    if self.array[idx] < self.array[left]:
                        self.array[idx], self.array[left] = (
                            self.array[left],
                            self.array[idx],
                        )
                        idx = left
                    else:
                        break


heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(20)
heap.insert(4)
print(heap.array)
heap.pop()
print(heap.array)
