from collections import deque
import math
import sys

input = sys.stdin.readline
# print = sys.stdout.write

N = int(input())
M = int(input())

city = [[] for _ in range(N + 1)]
cost = [[math.inf for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    city[a].append(b)
    cost[a][b] = min(cost[a][b], c)
# print(city)
start, end = map(int, input().split())

visit = [math.inf for _ in range(N + 1)]
q = deque()
q.append(start)
visit[start] = 0
while q:
    cursor = q.popleft()
    for Next in city[cursor]:
        if visit[Next] > visit[cursor] + cost[cursor][Next]:
            visit[Next] = visit[cursor] + cost[cursor][Next]
            q.append(Next)
# print(visit)
print(visit[end])
