from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

N, M = map(int, input().split())
Map = []

for i in range(N):
    s = input()
    Map.append(list(s))

# print(Map)

visit = [[9999999 for _ in range(M)] for _ in range(N)]
# print(visit)

q = deque()
q.append((0, 0))
visit[0][0] = 1

while q:
    x, y = q.popleft()

    for i in range(4):

        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < M and 0 <= ty < N and Map[ty][tx] == "1" and visit[ty][tx] > visit[y][x] + 1:
            visit[ty][tx] = visit[y][x] + 1
            q.append((tx, ty))

# for i in range(N):
#     print(visit[i])

print(visit[N-1][M-1])