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
        for Won in range(N, 0, -1):
            for i in range(1, 10000):
                # print("coin: ", coin[0] * i)
                if coin * i > Won:
                    break
                if Won - coin * i >= 0:
                    dp[Won] += dp[Won - coin * i]
        # print(dp)
    print(dp[N])
