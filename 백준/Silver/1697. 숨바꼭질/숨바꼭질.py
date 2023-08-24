import sys
from collections import deque

input = sys.stdin.readline

start, end = map(int, input().split())

q = deque()
visit = [99999999] * 100001

q.append((start, 0))
visit[start] = 0
while q:
    cur, time = q.popleft()
    # print(cur)
    if 0 <= cur + 1 <= 100000 and visit[cur + 1] > time + 1:
        visit[cur + 1] = time + 1
        q.append((cur + 1, time + 1))
    if 0 <= cur - 1 <= 100000 and visit[cur - 1] > time + 1:
        visit[cur - 1] = time + 1
        q.append((cur - 1, time + 1))
    if 0 <= cur * 2 <= 100000 and visit[cur * 2] > time + 1:
        visit[cur * 2] = time + 1
        q.append((cur * 2, time + 1))

print(visit[end])
