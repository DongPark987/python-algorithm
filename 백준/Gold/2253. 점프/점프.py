import math
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

isSmall = [False] * (N + 1)

for _ in range(M):
    isSmall[int(input())] = True

# 각 지점에서 가질 수 있는 모든 속도의 경우 * 지점의 수
dp = [[math.inf for _ in range(int((2 * N) ** 0.5) + 2)]
      for _ in range(N + 1)]

# 1번째 위치에서는 속도가 0이고 횟수도 0회이다.
dp[1][0] = 0

# 각각 위치에서의 최소 점프 횟수를 앞에서부터 한번씩 방문하며 계산한다.
for loc in range(2, N + 1):
    # 작은돌로는 점프하지 않는다.
    if isSmall[loc]: continue

    # 1 ~ 현재 위치에서 가질 수 있는 최대 속도까지 반복
    for speed in range(1, int((2 * loc) ** 0.5) + 1):
        #  1(증가한 점프 횟수) + 이전까지의 점프중 최소횟수
        dp[loc][speed] = 1 + min(dp[loc - speed][speed - 1],  # 속도를 1 증가시키며 점프했었음
                                 dp[loc - speed][speed],  # 속도를 유지하며 점프했었음
                                 dp[loc - speed][speed + 1])  # 속도를 감소시키며 점프했었음

if min(dp[N]) == math.inf:
    print(-1)
else:
    print(min(dp[N]))