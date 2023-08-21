from collections import deque
import math
import sys

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

N = int(input())
board = []
for _ in range(N):
    tmp = list(map(int, list(input())))
    board.append(tmp)
# print(board)

for drill in range(10000):
    visit = [[-1 for _ in range(N)] for _ in range(N)]

    q = deque()
    q.append((0, 0, drill))
    visit[0][0] = drill
    while q:
        x, y, d = q.popleft()
        for i in range(4):
            tx, ty = x + dx[i], y + dy[i]
            if 0 <= tx < N and 0 <= ty < N:
                if visit[ty][tx] < d:
                    if board[ty][tx] == 0:
                        if d > 0:
                            q.append((tx, ty, d - 1))
                            visit[ty][tx] = d
                    else:
                        q.append((tx, ty, d))
                        visit[ty][tx] = d

    if visit[N - 1][N - 1] != -1:
        print(drill)
        break
