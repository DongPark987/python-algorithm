import sys
from heapq import heappop, heappush

input = sys.stdin.readline

N = int(input().rstrip())

myHeap = []
for _ in range(N):
    tmp = int(input().rstrip())
    heappush(myHeap, tmp)
ans = 0
for _ in range(N - 1):
    tmp1 = int(heappop(myHeap))
    tmp2 = int(heappop(myHeap))
    ans += (tmp1 + tmp2)
    heappush(myHeap, tmp1 + tmp2)

print(ans)
