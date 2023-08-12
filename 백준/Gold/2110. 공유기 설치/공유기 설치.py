import sys

input = sys.stdin.readline
# print = sys.stdout.write

N, C = map(int, (input().rstrip().split()))
global arr
global ans
ans = 0
arr = []

for _ in range(N):
    arr.append(int(input().rstrip()))

arr.sort()

# print(arr)


def check(distance):
    global arr
    start = arr[0]
    cnt = 1
    for i in range(N - 1):
        if arr[i + 1]-start >= distance:
            # print(arr[i + 1])
            cnt += 1
            start = arr[i + 1]
    return cnt


def search(left, right, target):
    if left > right:
        return

    global arr
    global ans
    mid = (left + right) // 2

    cnt = check(mid)
    # print(mid, cnt)
    if cnt >= target:
        ans = max(ans, mid)
        search(mid + 1, right, target)
    else:
        search(left, mid - 1, target)
    return


search(0, arr[N - 1], C)
print(ans)

# print(check(3))