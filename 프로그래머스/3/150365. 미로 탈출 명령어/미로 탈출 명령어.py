from collections import deque
import math
import sys
sys.setrecursionlimit(5000)

dy = [0, -1, 1, 0]
dx = [1, 0, 0, -1]
dAlpha = ['d', 'l', 'r', 'u']


def solution(n, m, x, y, r, c, k):
    visit = [[[False for _ in range(m + 1)] for _ in range(n + 1)] for _ in range((m + 1) * (n + 1))]
    answer = []

    def dfs(depth, curX, curY):
        # print(depth)
        # print(answer)
        # print(curX, r, curY, c, '-', depth)

        if depth > k:
            return False
        elif depth == k and curX == r and curY == c:
            return True
        for i in range(4):
            tx = curX + dx[i]
            ty = curY + dy[i]

            if 0 < tx <= n and 0 < ty <= m and not visit[depth][tx][ty]:
            # if 0 < tx <= n and 0 < ty <= m:
                # print(tx, ty)
                answer.append(dAlpha[i])
                visit[depth][tx][ty] = True
                if dfs(depth + 1, tx, ty):
                    return True
                answer.pop()

    dfs(0, x, y)
    if len(answer) == 0:
        return 'impossible'
    else:
        return ''.join(answer)