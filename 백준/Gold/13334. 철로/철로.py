import heapq
import sys
input = sys.stdin.readline
N = int(input())

people = []

for _ in range(N):
    tmp = list(map(int, input().split()))
    tmp.sort()
    people.append(tmp)
length = int(input())

people.sort(key=lambda x: (x[1]))

pq = []
ans = 0
for i in people:
    if i[1] - i[0] <= length:
        heapq.heappush(pq, i[0])

    while len(pq) != 0:
        if i[1] - pq[0] > length:
            heapq.heappop(pq)
        else:
            ans = max(len(pq), ans)
            break

print(ans)
