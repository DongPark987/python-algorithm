import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

link = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    link[a].append(b)
    link[b].append(a)
# print(link)


visit = [False for _ in range(N + 1)]
ans = 0
for i in range(1, N + 1):
    if visit[i]: continue
    ans += 1
    myQueue = deque()
    myQueue.append(i)
    visit[i] = True
    while myQueue:
        size = len(myQueue)
        for _ in range(size):
            front = myQueue.popleft()
            for j in link[front]:
                if not visit[j]:
                    myQueue.append(j)
                    visit[j] = True
print(ans)
