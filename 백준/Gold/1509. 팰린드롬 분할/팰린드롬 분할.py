import sys
import math

input = sys.stdin.readline

arr = list(input().rstrip())
# print(arr)
N = len(arr)

dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

ans = 0

for i in range(N):
    ans += 1
    dp[i][i] = 1
for i in range(N - 1):
    if arr[i] == arr[i + 1]:
        ans += 1
        dp[i][i + 1] = 1

for gap in range(2, N):
    for i in range(N - gap):
        if arr[i] == arr[i + gap]:
            if dp[i + 1][i + gap - 1] == 1:
                ans += 1
                dp[i][i + gap] = 1

# for i in range(N):
#     print(dp[i])

PLength = [99999] * (N + 1)
PLength[-1] = 0
for end in range(N):
    for start in range(end + 1):
        if dp[start][end]:
            PLength[end] = min(PLength[end], PLength[start - 1] + 1)
        else:
            PLength[end] = min(PLength[end], PLength[end - 1] + 1)
print(PLength[N - 1])
