import sys
import math

n, k = map(int, input().split())

coin = []
for _ in range(n):
    a = int(input())
    coin.append(a)
ans = [math.inf] * 10001
ans[0] = 0

for i in range(1, k + 1):
    for j in range(n):
        if i - coin[j] >= 0:
            ans[i] = min(ans[i], ans[i - coin[j]] + 1)

if ans[k] == math.inf:
    print(-1)
else:
    print(ans[k])
