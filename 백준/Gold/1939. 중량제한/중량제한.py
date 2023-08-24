import sys
from collections import deque
import math
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())

edge = [{} for _ in range(N + 1)]
visit = [0 for _ in range(N + 1)]


for _ in range(M):
    a, b, c = map(int, input().split())
    if edge[a].get(b) is None:
        edge[a][b] = c
        edge[b][a] = c
    else:
        if edge[a][b] < c:
            edge[a][b] = c
            edge[b][a] = c

start, end = map(int, input().split())

hq = []
heapq.heappush(hq, (-math.inf, start))
# q.append(start)
visit[start] = math.inf

while hq:
    hcost, cur = heapq.heappop(hq)
    for Next, Cost in edge[cur].items():
        if visit[Next] < visit[cur] and visit[Next] < Cost:
            if visit[cur] > Cost:
                visit[Next] = Cost
                heapq.heappush(hq, (-Cost, Next))
            else:
                visit[Next] = visit[cur]
                heapq.heappush(hq, (-visit[cur], Next))

print(visit[end])