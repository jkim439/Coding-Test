class Heap:
    def __init__(self, value):
        self.array = [None, value]

    def push(self, value):
        self.array.append(value)
        i = len(self.array) - 1

        while 1:
            parent = i // 2

            if i <= 1:
                break

            else:
                if self.array[i] > self.array[parent]:
                    self.array[i], self.array[parent] = (
                        self.array[parent],
                        self.array[i],
                    )
                    i = parent
                else:
                    break

    def pop(self):
        print(self.array[1])
        self.array[1], self.array[-1] = self.array[-1], self.array[1]
        del self.array[-1]

        i = 1

        while 1:
            left = i * 2
            right = left + 1

            if len(self.array) - 1 < left:
                break

            elif left < len(self.array) <= right:
                if self.array[i] < self.array[left]:
                    self.array[i], self.array[left] = (
                        self.array[left],
                        self.array[i],
                    )
                    i = left
                else:
                    break

            else:
                if self.array[left] < self.array[right]:
                    if self.array[i] < self.array[right]:
                        self.array[i], self.array[right] = (
                            self.array[right],
                            self.array[i],
                        )
                        i = right
                    else:
                        break
                else:
                    if self.array[i] < self.array[left]:
                        self.array[i], self.array[left] = (
                            self.array[left],
                            self.array[i],
                        )
                        i = left
                    else:
                        break


heap = Heap(15)
heap.push(10)
heap.push(8)
heap.push(5)
heap.push(20)
heap.push(4)
print(heap.array)
heap.pop()
print(heap.array)
