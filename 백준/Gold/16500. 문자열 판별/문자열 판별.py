from functools import cache
S = input()
A = []

for i in range(int(input())):
    A.append(input())
dp = [0] * 101

@cache
def rec(cur):
    global S

    for word in A:
        length = len(word)
        # print(S[cur:cur + length], word)
        if S[cur:cur + length] == word:
            for K in range(cur, cur + length):
                dp[K] = 1
            rec(cur + length)

    return


rec(0)
# print(dp)
print(dp[len(S) - 1])
