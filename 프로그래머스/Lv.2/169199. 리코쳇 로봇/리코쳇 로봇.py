from collections import deque
import math

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def solution(board):
    h = len(board)
    w = len(board[0])
    visit = [[math.inf for _ in range(w)] for _ in range(h)]
    R = ()
    G = ()
    ans = math.inf
    for row in range(h):
        for col in range(w):
            if board[row][col] == 'R':
                R = (row, col)
            elif board[row][col] == 'G':
                G = (row, col)
    # print(R)
    # print(G)
    q = deque()
    q.append(R)
    visit[R[0]][R[1]] = 0
    while q:
        front = q.popleft()
        for i in range(4):
            tx = front[1] + dx[i]
            ty = front[0] + dy[i]
            cost = visit[front[0]][front[1]] + 1
            if tx < 0 or tx >= w or ty < 0 or ty >= h or board[ty][tx] == 'D':
                continue
            while True:
                # print((ty, tx), board[ty][tx])
                ttx = tx + dx[i]
                tty = ty + dy[i]
                if ttx < 0 or ttx >= w or tty < 0 or tty >= h or board[tty][ttx] == 'D':
                    if board[ty][tx] == 'G':
                        ans = min(ans, cost)
                    if visit[ty][tx] > cost:
                        visit[ty][tx] = cost
                        q.append((ty, tx))
                    visit[ty][tx] = min(visit[ty][tx], cost)
                    break
                visit[ty][tx] = min(visit[ty][tx], cost)
                tx, ty = ttx, tty

    # for i in board:
    #     print(i)
    # print()
    # for i in visit:
    #     print(i)
    if ans == math.inf:
        return -1
    else:
        return ans