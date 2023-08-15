from itertools import combinations, permutations
import sys
import math

input = sys.stdin.readline
print = sys.stdout.write

global N, arr, visit, ans, start
N = int(input().rstrip())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
visit = [False for i in range(N)]
ans = math.inf
Start = 0


def dfs(loc, sum, before):
    global arr, visit, ans, Start

    if (loc == N - 1):
        if arr[before][Start] != 0:
            sum += arr[before][Start]
            ans = min(ans, sum)
            return
        return
    for i in range(N):
        if arr[before][i] == 0 or sum + arr[before][i] >= ans:
            continue
        if not visit[i]:
            visit[i] = True
            dfs(loc + 1, sum + arr[before][i], i)
            visit[i] = False


for i in range(N):
    Start = i
    visit[i] = True
    dfs(0, 0, i)
    visit[i] = False

print(str(ans))