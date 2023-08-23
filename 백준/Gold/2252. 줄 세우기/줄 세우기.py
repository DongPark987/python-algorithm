import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

Link = [[] for _ in range(N)]

parent = [0] * N

for _ in range(M):
    a, b = map(int, input().split())
    Link[a - 1].append(b - 1)
    parent[b - 1] += 1

q = deque()

for i in range(N):
    if parent[i] == 0:
        q.append(i)

while q:
    cur = q.popleft()
    print(cur+1, end=" ")
    for i in Link[cur]:
        parent[i] -= 1
        if parent[i] == 0:
            q.append(i)
