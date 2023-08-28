import sys
import math

input = sys.stdin.readline

N, M = map(int, input().split())

dp = []

for _ in range(N):
    dp.append(list(map(int, input().split())))

# print(arr)

for j in range(1, M):
    dp[0][j] += dp[0][j - 1]

for Row in range(1, N):
    LR = dp[Row][:]
    RL = dp[Row][:]
    for i in range(M):
        if i == 0:
            LR[i] += dp[Row - 1][i]
        else:
            LR[i] += max(dp[Row - 1][i], LR[i - 1])

    for i in range(M - 1, -1, -1):
        if i == M - 1:
            RL[i] += dp[Row - 1][i]
        else:
            RL[i] += max(dp[Row - 1][i], RL[i + 1])
    for i in range(M):
        dp[Row][i] = max(RL[i], LR[i])

print(dp[N - 1][M - 1])
