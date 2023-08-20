import sys
from collections import deque

input = sys.stdin.readline

ComNum = int(input())
LinkNum = int(input())

Link = [[] for _ in range(ComNum + 1)]
for _ in range(LinkNum):
    a, b = map(int, input().split())
    Link[a].append(b)
    Link[b].append(a)

visit = [False for _ in range(ComNum + 1)]

ans = 0
visit[1] = True
q = deque()
q.append(1)

while q:
    front = q.popleft()
    for i in Link[front]:
        if not visit[i]:
            visit[i] = True
            q.append(i)
            ans += 1
print(ans)
