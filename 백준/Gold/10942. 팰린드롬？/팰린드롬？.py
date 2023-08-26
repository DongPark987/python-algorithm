import sys

input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))
# print(arr)

dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(N):
    dp[i][i] = 1
for i in range(N - 1):
    if arr[i] == arr[i + 1]:
        dp[i][i + 1] = 1

for gap in range(2, N):
    for i in range(N - gap):
        if arr[i] == arr[i + gap]:
            if dp[i + 1][i + gap - 1] == 1:
                dp[i][i + gap] = 1

# for i in range(N):
#     print(dp[i])

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(dp[a - 1][b - 1])
