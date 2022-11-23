# 운영체제에서 프로세스 스케쥴링에 사용됨

# 라이브러리
import queue

queue = queue.Queue()

queue.put("Samsung")
queue.put("Hyundai")

print(queue.qsize())

print(queue.get())
print(queue.get())

print(queue.qsize())

# 리스트
queue = []

queue.append("Samsung")
queue.append("Hyundai")

print(len(queue))

print(queue.pop(0))
print(queue.pop(0))

print(len(queue))
