from collections import deque
import math
import heapq
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

start, end = map(int, input().split())


hq = []
ans = [math.inf for i in cost[start]]
ans[start] = 0
heapq.heappush(hq, (0, start))
while hq:
    cursor = heapq.heappop(hq)
    if ans[cursor[1]] != cursor[0]: continue
    for i in city[cursor[1]]:
        if ans[i] > cost[cursor[1]][i] + cursor[0]:
            ans[i] = cost[cursor[1]][i] + cursor[0]
            heapq.heappush(hq, (ans[i], i))

# print(ans)
print(ans[end])




# #===========================
# visit = [math.inf for _ in range(N + 1)]
# q = deque()
# q.append(start)
# visit[start] = 0
# while q:
#     cursor = q.popleft()
#     for Next in city[cursor]:
#         if visit[Next] > visit[cursor] + cost[cursor][Next]:
#             visit[Next] = visit[cursor] + cost[cursor][Next]
#             q.append(Next)
# # print(visit)
# print(visit)
# print(visit[end])
