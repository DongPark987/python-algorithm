from collections import deque
import math
import sys

dx = [0, 0, -1, 1, 0, 0]
dy = [-1, 1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

# 가로, 세로, 높이
M, N, H = map(int, input().split())

tomato = [[[] for _ in range(N)] for _ in range(H)]
# print(tomato)
youngTomato = 0
for i in range(H):
    for j in range(N):
        tmp = list(map(int, input().split()))
        for k in tmp:
            if k == 0:
                youngTomato += 1
            tomato[i][j].append(k)

if youngTomato == 0:
    print(0)
    exit()


# print(youngTomato)


# for i in range(H):
#     for j in range(N):
#         print(tomato[i][j])

def check(x, y, z):
    global H, N, M, tomato
    if 0 <= x < M and 0 <= y < N and 0 <= z < H and tomato[z][y][x] == 0:
        return True
    else:
        return False


q = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == 1:
                q.append((i, j, k))
for day in range(1, 1000000):
    beforeYoung = youngTomato
    qSize = len(q)
    for _ in range(qSize):
        z, y, x = q.popleft()
        for d in range(6):
            tx, ty, tz = x + dx[d], y + dy[d], z + dz[d]
            if check(tx, ty, tz):
                q.append((tz, ty, tx))
                if tomato[tz][ty][tx] == 0:
                    tomato[tz][ty][tx] = 1
                    youngTomato -= 1

    if youngTomato == 0:
        print(day)
        break
    else:
        # print(beforeYoung, youngTomato)
        if beforeYoung == youngTomato:
            print(-1)
            break

# for i in range(H):
#     for j in range(N):
#         print(tomato[i][j])


# if visit[i][j][k] or not tomato[i][j][k] == 1:
#     continue
# q = deque()
# # z,y,x
# q.append((i, j, k))
# visit[i][j][k] = True
# while q:
#     z, y, x = q.popleft()
#     # print(q)
#     for d in range(6):
#         tx, ty, tz = x + dx[d], y + dy[d], z + dz[d]
#         if check(tx, ty, tz) and not visit[tz][ty][tx]:
#             q.append((tz, ty, tx))
#             visit[tz][ty][tx] = True
#             if tomato[tz][ty][tx] == 0:
#                 tomato[tz][ty][tx] = 1
#                 youngTomato -= 1
