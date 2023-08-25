import sys

input = sys.stdin.readline

N = int(input())
k = int(input())

arr = []
dp = [0 for _ in range(N + 1)]
dp[0] = 1

for _ in range(k):
    arr.append(list(map(int, input().split())))

for coin in arr:
    for Won in range(N, 0, -1):
        for i in range(1, coin[1] + 1):
            # print("coin: ", coin[0] * i)
            if Won - coin[0] * i >= 0:
                dp[Won] += dp[Won - coin[0] * i]
    # print(dp)
print(dp[N])


