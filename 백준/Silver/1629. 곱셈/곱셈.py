import sys

input = sys.stdin.readline

A, B, C = map(int, input().split())


def rec(B):
    if B == 1:
        # A^1 mod C
        return A % C

    k = rec(B // 2) % C
    if B % 2 == 0:
        #k => A//2 mod C
        #((A^B//2 mod C) * (A^B//2 mod C)) mod C
        return k * k % C
    else:
        # k => A//2 mod C
        # ((A^B//2 mod C) * (A^B//2 mod C) * (A^1 mod C)) mod C
        return k * k % C * A % C


print(rec(B))
