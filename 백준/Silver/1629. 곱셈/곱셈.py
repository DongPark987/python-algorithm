import sys

input = sys.stdin.readline

A, B, C = map(int, input().split())


def rec(B):
    if B == 1:
        return A % C

    k = rec(B // 2) % C
    if B % 2 == 0:
        return k * k % C
    else:
        return k * k % C * A % C


print(rec(B))
