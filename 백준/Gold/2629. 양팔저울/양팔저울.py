from functools import cache


M = int(input())
Iron = list(map(int, input().split()))

N = int(input())
Ball = list(map(int, input().split()))

Iron.append(0)
# print(Ball)
# print(Iron)

dp = [[False for _ in range(15001)] for _ in range(31)]


@cache
def rec(i, weight):
    if i > M or dp[i][weight]:
        return
    dp[i][weight] = True
    rec(i + 1, weight)
    rec(i + 1, weight + Iron[i])
    rec(i + 1, abs(weight - Iron[i]))


rec(0, 0)
# print(dp)
for ball in Ball:
    if ball> 15000:
        print("N")
    elif dp[M][ball]:
        print("Y")
    else:
        print("N")
