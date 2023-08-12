import sys

# input = sys.stdin.readline
# print = sys.stdout.write
N, M = map(int, (input().rstrip().split()))
arr = list(map(int, input().rstrip().split()))

arr.sort(reverse=True)
global ans
ans = 0


# 이분 탐색 구현
def search(left, right, target):
    global ans
    if left > right:
        return 0
    mid = (left + right) // 2

    mySum = 0
    for i in arr:
        if i <= mid:
            break
        else:
            mySum += (i - mid)

    if mySum >= target:
        ans = max(ans, mid)

    if mySum < target:
        return search(left, mid - 1, target)
    else:
        return search(mid + 1, right, target)


search(0, arr[0], M)
print(int(ans))
