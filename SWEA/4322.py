##################################################
import sys

sys.stdin = open(sys.argv[0][:-3] + ".txt", "r")
##################################################

for t in range(1, int(input())):
    # n = int(input())
    # packets = [list(map(int, input().split())) for _ in range(n)]
    n = 3
    packets = [[1, 5], [2, 4], [3, 8]]
    # print(n, packets)

    if sum([i[1] for i in packets]) <= 10:
        print(f"#{t} {1}")

    c = 2
    r = 0
    while c <= 5:
        next = []
        packets.sort(key=lambda x: (x[0] + x[1], -x[0]), reverse=True)
        # print(packets)
        while packets:
            s, l = packets.pop(0)
            if r < c:
                r += 1
                next.append(s + l)
            else:
                time = min(next) - s + l
                next.append(min(next) + l)
                next.remove(min(next))
                if time > 10:
                    c += 1
                    break
                else:
                    r += 1
        if r == n:
            print(f"#{t} {c}")
            break
