import sys

input = sys.stdin.readline
N, M = map(int, input().split())
edge = [set() for _ in range(N + 1)]
# print(edge)

for _ in range(M):
    a, b = map(int, input().split())
    edge[b].add(a)
visitCnt = [0 for _ in range(N + 1)]
brotherCnt = [0 for _ in range(N + 1)]


def dfs(node, visit):
    visitCnt[node] += 1
    visit[node] = True
    cnt = 1
    for i in edge[node]:
        if visit[i]:
            continue
        cnt += dfs(i, visit)
    return cnt


for i in range(1, N + 1):
    visit = [False for _ in range(N + 1)]
    brotherCnt[i] = dfs(i, visit)
mid = N // 2
ans = 0
for i in range(1, N + 1):
    if visitCnt[i] - 1 > mid or brotherCnt[i] - 1 > mid:
        ans += 1
# print(visitCnt)
# print(brotherCnt)
print(ans)
