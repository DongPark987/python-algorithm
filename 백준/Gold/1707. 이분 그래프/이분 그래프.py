import sys
from collections import deque

input = sys.stdin.readline


def cross(a):
    if a == 1:
        return 2
    else:
        return 1


K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    arr = [[] for _ in range(V)]

    for _ in range(E):
        a, b = map(int, input().split())
        arr[a - 1].append(b - 1)
        arr[b - 1].append(a - 1)

    isYes = True
    # print(arr)
    visit = [0 for _ in range(V)]
    for i in range(V):
        if visit[i] != 0: continue
        q = deque()
        q.append(i)
        visit[i] = 1
        while q:
            front = q.popleft()
            # print("front: ",front)
            for link in arr[front]:
                if visit[link] == 0:
                    # print(front, link, cross(visit[front]))
                    visit[link] = cross(visit[front])
                    q.append(link)
                elif visit[link] == visit[front]:
                    # print(link, front)
                    isYes = False
                    break
            if not isYes:
                break

    # print(visit)
    if isYes:
        print("YES")
    else:
        print("NO")
