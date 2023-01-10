# 무인도 탈출
for t in range(1, int(input()) + 1):
    n = int(input())
    boxes = []
    for i in range(n):
        box = list(map(int, input().split()))
        boxes.append([box[0], box[1], box[2], i])
        boxes.append([box[0], box[2], box[1], i])
        boxes.append([box[1], box[2], box[0], i])

    boxes = sorted(boxes, key=lambda x: x[0] * x[1])

    height = [box[2] for box in boxes]
    visit = [[box[3]] for box in boxes]

    for i in range(3 * n):
        for j in range(i - 1, -1, -1):
            if boxes[i][3] in visit[j]:
                continue
            if (boxes[i][0] >= boxes[j][0] and boxes[i][1] >= boxes[j][1]) or (
                boxes[i][0] >= boxes[j][1] and boxes[i][1] >= boxes[j][0]
            ):
                if height[i] < boxes[i][2] + height[j]:
                    height[i] = boxes[i][2] + height[j]
                    visit[i] = visit[j] + [boxes[i][3]]

    answer = max(height)
    print(f"#{t} {answer}")
