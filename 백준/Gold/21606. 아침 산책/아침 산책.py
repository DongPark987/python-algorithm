import sys
from collections import deque
import math

input = sys.stdin.readline

N = int(input().rstrip())
color = input().rstrip()
color = list(color)
# print(color)

edge = [[] for _ in range(N)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    edge[a - 1].append(b - 1)
    edge[b - 1].append(a - 1)

ans = 0
MainVisit = [False] * N

q = deque()
for i in range(N):

    if MainVisit[i] or color[i] == '0': continue
    # print("round",i)
    visit = [False] * N
    q.append(i)
    visit[i] = True
    MainVisit[i] = True
    cnt = 1
    while q:
        front = q.popleft()
        for i in edge[front]:
            if not visit[i]:
                visit[i] = True
                MainVisit[i] = True
                if color[i] == '1':
                    cnt += 1
                else:
                    q.append(i)

    # print("cnt:", cnt)
    ans += cnt * (cnt - 1)
    # print()
    # for j in range(N):
    #     print(MainVisit[j])
    # print()

print(ans)
