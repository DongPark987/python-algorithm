import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))

dp = [0] * (M + 1)

for w, v, k in arr:
    cur = 1
    ManJockDo = []
    while k > 0:
        tmp = min(cur,k)
        ManJockDo.append(tmp)
        cur *= 2
        k -= tmp
    # print(ManJockDo)
    for pick in ManJockDo:
        for weight in range(M, 0, -1):
            if weight < w * pick: break
            dp[weight] = max(dp[weight], dp[weight - w * pick] + v * pick)

print(dp[M])
