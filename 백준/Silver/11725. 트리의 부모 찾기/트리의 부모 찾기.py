import sys

input = sys.stdin.readline
print = sys.stdout.write
sys.setrecursionlimit(10**6)
N = int(input())
tree = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

for i in tree:
    i.sort()
ans = [0 for _ in range(N + 1)]

visit = [False for _ in range(N + 1)]


def dfs(loc, parent):
    if visit[loc]:
        return
    ans[loc] = parent
    visit[loc] = True
    for i in tree[loc]:
        dfs(i, loc)


dfs(1, 0)

for i in range(2,N+1):
    print(str(ans[i])+"\n")
