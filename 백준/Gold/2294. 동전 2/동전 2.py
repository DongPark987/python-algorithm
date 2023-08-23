import sys
import math

n, k = map(int, input().split())

coin = []
for _ in range(n):
    a = int(input())
    coin.append(a)
ans = [999999] * 10001
ans[0] = 0

for won in range(1, k + 1):
    for j in range(n):
        if won - coin[j] >= 0:
            ans[won] = min(ans[won], ans[won - coin[j]] + 1)

if ans[k] == 999999:
    print(-1)
else:
    print(ans[k])
