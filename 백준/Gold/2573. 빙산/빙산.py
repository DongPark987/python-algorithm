import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

board = []

# 행, 열
N, M = map(int, input().split())

islandCnt = 0
Max = 0
startX = 0
startY = 0
for i in range(N):
    board.append(list(map(int, input().split())))
    for j in range(M):
        if board[i][j] != 0:
            islandCnt += 1
        if board[i][j] > Max:
            Max = max(board[i][j], Max)
            startX, startY = j, i


# print(startX, startY, island)

def melt(island):
    global N, M, board, startY, startX
    visit = [[False for _ in range(M)] for _ in range(N)]
    for y in range(N):
        for x in range(M):
            if board[y][x] == 0: continue
            visit[y][x] = True
            for i in range(4):
                tx = x + dx[i]
                ty = y + dy[i]
                if 0 <= tx < M and 0 <= ty < N and board[ty][tx] == 0 and not visit[ty][tx]:
                    board[y][x] -= 1
                    if board[y][x] == 0:
                        island -= 1
                        break
            if board[y][x] != 0:
                startY = y
                startX = x

    return island


# print(islandCnt)
# islandCnt = melt(islandCnt)
# print(islandCnt)

for round in range(0, 1100000):
    cnt = 1
    if board[startY][startX] == 0: continue
    visit = [[False for _ in range(M)] for _ in range(N)]
    q = deque()
    q.append((startX, startY))
    visit[startY][startX] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            tx, ty = x + dx[i], y + dy[i]
            if 0 <= tx < M and 0 <= ty < N and board[ty][tx] != 0 and not visit[ty][tx]:
                q.append((tx, ty))
                visit[ty][tx] = True
                cnt += 1
    # print()
    # for i in board:
    #     print(i)
    # print()
    # print(islandCnt, cnt)
    if islandCnt != cnt:
        print(round)
        exit()
    islandCnt = melt(islandCnt)
    if islandCnt == 0:
        break
    # print(islandCnt, cnt)

print(0)

# for i in board:
#     print(i)
