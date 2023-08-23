import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())
Link = [[] for _ in range(N)]
parentCnt = [0] * N
ans = [0] * N

for _ in range(M):
    a, b, c = map(int, input().split())
    Link[a - 1].append([b - 1, c])
    parentCnt[b - 1] += 1

q = deque()
q.append(N - 1)
ans[N - 1] = 1
# print("parent", parentCnt)
# print("Link", Link)
# print("ans", ans)
while q:
    # print("parent", parentCnt)
    # print("Link", Link)
    # print("ans", ans)
    #0 = nex, 1 =
    cur = q.popleft()
    for i in Link[cur]:
        ans[i[0]] += i[1] * ans[cur]
        parentCnt[i[0]] -= 1
        if parentCnt[i[0]] == 0:
            q.append(i[0])

# print(ans)
for i in range(N):
    if len(Link[i]) == 0 and ans[i] != 0:
        print(i + 1, ans[i])
