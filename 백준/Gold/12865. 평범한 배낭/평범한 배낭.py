import sys

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
items = [list(map(int, input().rstrip().split())) for _ in range(N)]

dp = [0 for _ in range(K + 1)]

for item in items:
    for weight in range(K, -1, -1):
        if weight - item[0] >= 0:
            dp[weight] = max(dp[weight], item[1] + dp[weight - item[0]])
        else:
            break
print(dp[K])