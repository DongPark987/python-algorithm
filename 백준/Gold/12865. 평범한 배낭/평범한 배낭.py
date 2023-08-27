N, K = map(int, input().split())

arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))

# print(arr)

dp = [0] * (K + 1)

for w, v in arr:
    for weight in range(K, 0, -1):
        if weight < w: break
        dp[weight] = max(dp[weight], dp[weight - w] + v)

# print(dp)
print(dp[K])
