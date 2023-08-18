from collections import deque

DIR = [[0, -1], [1, 0], [0, 1], [-1, 0]]
cd = [[3, 0, 1, 2], [1, 2, 3, 0]]


class Baem:
    def __init__(self):
        self.dir = 0
        self.y = 0
        self.x = 0
        self.change = -1

    def set(self, x, y, dir, change):
        self.x = x
        self.y = y
        self.dir = dir
        self.change = change


N = int(input())

arr = [[0 for _ in range(N)] for _ in range(N)]

K = int(input())

for _ in range(K):
    y, x = map(int, input().split())
    arr[y - 1][x - 1] = 1

L = int(input())
baemMove = deque()
for _ in range(L):
    baemMove.append((input().split()))

baemBody = []
a = Baem()
a.set(0, 0, 1, -1)
baemBody.append(a)
# print(baemBody[0].dir)
# print(baemBody[0].x, baemBody[0].y)
ans = 0
Timer = 1
arr[0][0] = 2
move = deque()
isDie = False
while True:
    if isDie:
        break
    # 방향전환 체크
    if len(baemMove) != 0:
        tmpMove = baemMove.popleft()
        # print("방향체크", tmpMove[0], Timer)
        if int(tmpMove[0]) == Timer - 1:
            # print("전환 시작")
            if tmpMove[1] == 'L':
                # print("방향전환", cd[0][baemBody[0].dir])
                next = cd[0][baemBody[0].dir]
                # baemBody[0].dir = next
                baemBody[0].dir = next
            else:
                # print("방향전환", cd[1][baemBody[0].dir])
                next = cd[1][baemBody[0].dir]
                # baemBody[0].dir = next
                baemBody[0].dir = next
        else:
            baemMove.appendleft(tmpMove)
    # 뱀 움직임
    idx = 0
    isEat = False
    newBody = Baem()
    for b in baemBody:
        arr[b.y][b.x] = 0
        # print(b.dir)
        ty = b.y + DIR[b.dir][1]
        tx = b.x + DIR[b.dir][0]
        # print(b.x, b.y)

        # 뱀뒤짐
        if tx < 0 or tx >= N or ty < 0 or ty >= N or arr[ty][tx] == 2:
            isDie = True
            # print("디짐")
            ans = Timer
            break
        # 사과 먹음
        if arr[ty][tx] == 1:
            isEat = True
            lastBody = baemBody[-1]
            newBody.set(lastBody.x, lastBody.y, lastBody.dir, -1)
        b.y = ty
        b.x = tx
        arr[b.y][b.x] = 2
        idx += 1

    # 방향전환 전달
    if len(baemBody) != 1:
        for i in range(len(baemBody) - 1, 0, -1):
            baemBody[i].dir = baemBody[i - 1].dir
    if isEat:
        baemBody.append(newBody)

    Timer += 1
    # print("회차: ", Timer)
    # for i in arr:
    #     print(i)
    # print()

print(ans)
