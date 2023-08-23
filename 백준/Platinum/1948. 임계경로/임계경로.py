from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

Link = [[] for _ in range(n + 1)]
RLink = [[] for _ in range(n + 1)]
parentCnt = [0 for _ in range(n + 1)]

for i in range(m):
    a, b, c = map(int, input().split())
    Link[a].append([b, c])
    RLink[b].append([a, c])
    parentCnt[a] += 1

# print(RLink)

start, end = map(int, input().split())

q = deque()
q.append(end)
MaxLength = [0 for _ in range(n + 1)]
MaxLength[end] = 0
MaxPerson = []
while q:
    cur = q.popleft()
    for Next, Cost in RLink[cur]:
        MaxLength[Next] = max(MaxLength[Next], MaxLength[cur] + Cost)
        parentCnt[Next] -= 1
        if Next == start:
            MaxPerson.append([Next, cur, MaxLength[cur] + Cost])
        if parentCnt[Next] == 0:
            q.append(Next)

ans = 0
q.append(start)
visit = [False] * (n + 1)
while q:
    cur = q.popleft()
    for Next, Cost in Link[cur]:
        if MaxLength[cur] - Cost == MaxLength[Next]:
            ans += 1
            if not visit[Next]:
                q.append(Next)
                visit[Next] = True

print(MaxLength[start])
print(ans)
