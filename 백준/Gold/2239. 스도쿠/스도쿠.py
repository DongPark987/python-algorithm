import sys

board = []
visit = [[False for _ in range(10)] for _ in range(10)]
area_visit = [[[False for _ in range(10)] for _ in range(3)] for _ in range(3)]

row_set = [set() for _ in range(9)]
col_set = [set() for _ in range(9)]

for _ in range(9):
    line = list(map(int, list(sys.stdin.readline().rstrip())))
    board.append(line)

for i in range(9):
    for j in range(9):
        a_i = i // 3
        a_j = j // 3
        row_set[i].add(board[i][j])
        col_set[j].add(board[i][j])
        area_visit[a_i][a_j][board[i][j]] = True



def dfs(loc):
    if loc == 81:
        for i in range(9):
            print(''.join(str(s) for s in board[i]))
        exit()
    board_x = loc % 9
    board_y = loc // 9
    a_x = board_x // 3
    a_y = board_y // 3
    if board[board_y][board_x] == 0:
        for i in range(1, 10):
            if not area_visit[a_y][a_x][i] and i not in row_set[board_y] and i not in col_set[board_x]:
                area_visit[a_y][a_x][i] = True
                row_set[board_y].add(i)
                col_set[board_x].add(i)
                board[board_y][board_x] = i
                dfs(loc + 1)
                board[board_y][board_x] = 0
                area_visit[a_y][a_x][i] = False
                row_set[board_y].remove(i)
                col_set[board_x].remove(i)
    else:
        dfs(loc + 1)

dfs(0)