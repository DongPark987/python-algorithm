import sys
import heapq

input = sys.stdin.readline
print = sys.stdout.write

N = int(input().rstrip())

heap = []

# print(str(N))

for _ in range(N):
    tmp = int(input().rstrip())
    if tmp == 0:
        if len(heap) != 0:
            print(str(-heapq.heappop(heap)) + "\n")
        else:
            print("0\n")
    else:
        heapq.heappush(heap,-tmp)
