from itertools import combinations, permutations
import sys
input = sys.stdin.readline
print = sys.stdout.write

global N
N = int(input().rstrip())
global arr
arr = []
global visit
visit = [False for i in range(N)]
global ans
ans = 1000000000
global Start
Start = 0

for _ in range(N):
    arr.append(list(map(int, input().rstrip().split())))


def dfs(loc, sum, pre):
    global arr
    global visit
    global ans
    global Start

    if (loc == N-1):
        if arr[pre][Start] != 0:
            sum += arr[pre][Start]
            ans = min(ans, sum)
            return
        return
    for i in range(N):
        if arr[pre][i] == 0 or sum + arr[pre][i] >= ans:
            continue
        if visit[i] == False:
            visit[i] = True
            dfs(loc+1, sum + arr[pre][i], i)
            visit[i] = False


for i in range(N):
    Start = i
    visit[i] = True
    dfs(0, 0, i)
    visit[i] = False


print(str(ans))
