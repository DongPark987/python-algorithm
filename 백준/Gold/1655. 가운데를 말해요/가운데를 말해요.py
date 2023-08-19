import sys
from heapq import heappush, heappop

input = sys.stdin.readline
print = sys.stdout.write

leftHeap = []
lCnt = 1
rightHeap = []
rCnt = 0

N = int(input().rstrip())

tmp = int(input().rstrip())
heappush(leftHeap, -tmp)
print(str(tmp) + '\n')

for _ in range(1,N):
    # print(leftHeap)
    # print(rightHeap)
    tmp = int(input().rstrip())
    if lCnt <= rCnt:
        if tmp > rightHeap[0]:
            heappush(leftHeap, -heappop(rightHeap))
            heappush(rightHeap, tmp)

        else:
            heappush(leftHeap, -tmp)
        lCnt += 1

    else:
        if tmp > -leftHeap[0]:
            heappush(rightHeap, tmp)
        else:
            heappush(rightHeap, -heappop(leftHeap))
            heappush(leftHeap, -tmp)
        rCnt += 1
    print(str(-leftHeap[0]) + '\n')
