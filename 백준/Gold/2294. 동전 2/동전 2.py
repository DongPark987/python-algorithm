import sys
import math

n, k = map(int, input().split())

coin = set()
for _ in range(n):
    a = int(input())
    coin.add(a)
ans = [999999] * 10001
ans[0] = 0

for won in range(1, k + 1):
    for c in coin:
        if won - c >= 0:
            ans[won] = min(ans[won], ans[won - c] + 1)

# print(ans)
if ans[k] == 999999:
    print(-1)
else:
    print(ans[k])
