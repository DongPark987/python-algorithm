import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())

myEdge = [[] for i in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    myEdge[a].append(b)
    myEdge[b].append(a)
for i in myEdge:
    i.sort()

# print(myEdge)

# DFS
myStack = []
visit = [False for i in range(N + 1)]


def dfs(loc):
    if visit[loc]:
        return
    print(loc, end=" ")
    visit[loc] = True
    for i in myEdge[loc]:
        dfs(i)


dfs(V)

print()

visit2 = [False for i in range(N + 1)]
myQueue = deque()
myQueue.append(V)
visit2[V] = True
while myQueue:
    size = len(myQueue)
    for _ in range(size):
        front = myQueue.popleft()
        print(front, end=" ")
        for i in myEdge[front]:
            if not visit2[i]:
                myQueue.append(i)
                visit2[i] = True
