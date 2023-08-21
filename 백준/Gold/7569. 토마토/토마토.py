from collections import deque
import math
import sys

input = sys.stdin.readline

dx = [0, 0, -1, 1, 0, 0]
dy = [-1, 1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

# 가로, 세로, 높이
M, N, H = map(int, input().split())
q = deque()
tomato = [[[] for _ in range(N)] for _ in range(H)]
# print(tomato)
youngTomato = 0
for i in range(H):
    for j in range(N):
        tmp = list(map(int, input().split()))
        for k in range(len(tmp)):
            if tmp[k] == 0:
                youngTomato += 1
            if tmp[k] == 1:
                q.append((i, j, k))
            tomato[i][j].append(tmp[k])

if youngTomato == 0:
    print(0)
    exit()

def check(x, y, z):
    global H, N, M, tomato
    if 0 <= x < M and 0 <= y < N and 0 <= z < H and tomato[z][y][x] == 0:
        return True
    else:
        return False

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
        if beforeYoung == youngTomato:
            print(-1)
            break
