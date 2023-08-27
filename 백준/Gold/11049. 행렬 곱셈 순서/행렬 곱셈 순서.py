import math
import sys
input = sys.stdin.readline

N = int(input())

dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

for Rng in range(1, N):
    for left in range(0, N - Rng):
        dp[left][left + Rng] = math.inf
        for cur in range(left, left + Rng):
            dp[left][left + Rng] = min(dp[left][left + Rng],
                                       dp[left][cur] +
                                       dp[cur + 1][left + Rng] +
                                       matrix[left][0] * matrix[cur][1] * matrix[left + Rng][1])

# print(matrix)
# for i in range(N):
#     print(dp[i])
print(dp[0][N - 1])
