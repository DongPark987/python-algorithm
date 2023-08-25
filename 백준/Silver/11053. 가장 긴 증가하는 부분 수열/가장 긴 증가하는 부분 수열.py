N = int(input())

data = list(map(int, input().split()))
dp = [0] * N

ans = 0
for i in range(1, N):
    for j in range(0, i):
        if data[i] > data[j]:
            dp[i] = max(dp[i], dp[j] + 1)
            ans = max(ans, dp[i])
print(ans + 1)
