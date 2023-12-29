dx = [0,0,1,-1]
dy = [1,-1,0,0]
def solution(board, h, w):
    answer = 0
    for i in range(4):
        ty = h + dy[i]
        tx = w + dx[i]
        if tx < 0 or tx >= len(board[0]) or ty < 0 or ty >= len(board):
            continue
        if board[h][w] == board[ty][tx]:
            answer += 1
    return answer