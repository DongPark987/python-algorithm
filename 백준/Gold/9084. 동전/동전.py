import sys

input = sys.stdin.readline

a = int(input())
for _ in range(a):
    k = int(input())
    arr = list(map(int, input().split()))
    N = int(input())

    dp = [0 for _ in range(N + 1)]
    dp[0] = 1

    for coin in arr:
        for i in range(coin, N+1):
            dp[i] += dp[i - coin]

    print(dp[N])
