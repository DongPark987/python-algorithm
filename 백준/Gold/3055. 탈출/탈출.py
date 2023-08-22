from collections import deque
import sys

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

input = sys.stdin.readline

# 행, 열
R, C = map(int, (input().split()))

board = [[] for _ in range(R)]

wq = deque()
gq = deque()
goal = 0
for i in range(R):
    tmp = list(input().rstrip())
    for j in range(C):
        if tmp[j] == 'D':
            goal = (j, i)
        elif tmp[j] == '*':
            wq.append((j, i))
        elif tmp[j] == 'S':
            gq.append((j, i))
        board[i].append(tmp[j])


# print(board)


def check(x, y):
    if 0 <= x < C and 0 <= y < R:
        return True
    else:
        return False


def flood():
    global wq, board
    size = len(wq)
    for _ in range(size):
        x, y = wq.popleft()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if check(tx, ty) and (board[ty][tx] == "." or board[ty][tx] == "S"):
                board[ty][tx] = '*'
                wq.append((tx, ty))


def dotchiRun():
    global gq, board
    size = len(gq)
    for _ in range(size):
        x, y = gq.popleft()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if check(tx, ty) and (board[ty][tx] == '.' or board[ty][tx] == 'D'):
                if (tx, ty) == goal:
                    return True

                isWater = False
                # print('tx,ty: ', tx, ty)
                for j in range(4):
                    ttx = tx + dx[j]
                    tty = ty + dy[j]
                    # print("ttx, tty: ", ttx, tty)
                    if check(ttx, tty) and board[tty][ttx] == "*":
                        # print(board[tty][ttx])
                        isWater = True
                if not isWater:
                    board[ty][tx] = 'S'
                    gq.append((tx, ty))
    return False


for i in range(1, 100000):
    if dotchiRun():
        print(i)
        break
    flood()
    if not gq:
        print('KAKTUS')
        break
