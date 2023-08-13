import sys

input = sys.stdin.readline
# print = sys.stdout.write
N, r, c = map(int, input().rstrip().split())
global ans
ans = 0


def rec(x, y, length):
    global ans
    half = length // 2
    # print(x, y, length)
    if r == y and c == x:
        print(ans)
        exit()
    if y <= r < y + length and x <= c < x + length:
        # print("a")
        rec(x, y, half)
        rec(x + half, y, half)
        rec(x, y + half, half)
        rec(x + half, y + half, half)
    else:
        ans += length ** 2


rec(0, 0, 2 ** N)