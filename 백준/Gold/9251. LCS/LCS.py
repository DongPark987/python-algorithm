a = [0] + list(input())
b = [0] + list(input())

dp = [[0 for _ in range(1001)] for _ in range(1001)]
for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i] == b[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            pass
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
            pass
print(dp[len(a) - 1][len(b) - 1])
