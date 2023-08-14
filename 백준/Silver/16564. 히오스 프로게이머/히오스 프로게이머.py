import sys

input = sys.stdin.readline

N, K = map(int, input().split())

global ans
ans = -1

global Min
Min = 2000000001

global arr
arr = []

for _ in range(N):
    arr.append(int(input()))

arr.sort(reverse=True)


def check(num):
    global ans
    global Min
    stock = K
    isTrue = True
    for i in arr:
        if stock - (num - i) >= 0:
            if i < num:
                stock -= num - i
        else:
            isTrue = False
            break
    if isTrue:
        return stock
    else:
        return 3000000001


def rec(left, right):
    # print(left, right)
    global Min, ans
    if left > right:
        return
    mid = (left + right) // 2
    tmp = check(mid)
    if tmp < Min:
        # print(f"tmp{tmp}")
        ans = mid
        Min = tmp
        rec(mid + 1, right)
    else:
        rec(left, mid - 1)


rec(0, arr[0] + K)

print(ans)
