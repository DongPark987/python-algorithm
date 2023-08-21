from collections import deque
import math
import sys

input = sys.stdin.readline
print = sys.stdout.write
# 노드, 길, 거리, 시작위치
N, M, K, X = map(int, input().split())

road = [[] for _ in range(1000000)]
for i in range(M):
    a, b = map(int, input().split())
    road[a - 1].append(b - 1)

visit = [math.inf for _ in range(300000)]

q = deque()

visit[X-1] = 0
q.append(X-1)
ans = 0
while q:
    cursor = q.popleft()
    for i in road[cursor]:
        if visit[i] > visit[cursor] + 1:
            if visit[cursor] < K:
                visit[i] = visit[cursor] + 1
                q.append(i)

isAns = False
for i in range(0, N):
    # print(str(visit[i])+"\n")

    if visit[i] == K:
        print(str(i+1)+"\n")
        isAns = True
if not isAns:
    print(str(-1))

# print(road)
