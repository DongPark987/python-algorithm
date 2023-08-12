import sys

input = sys.stdin.readline
# print = sys.stdout.write

global N
N = int(input().rstrip())
global arr
arr = list(map(int, input().rstrip().split()))

global gap
gap = 20000000001

global ans
ans = []

arr.sort()


def search(left, right, target):
    global N, arr, gap, ans
    if left > right:
        return
    mid = (left + right) // 2
    if abs(arr[mid] + target) < gap and arr[mid]!=target:
        gap = abs(arr[mid] + target)
        ans = [arr[mid], target]
    if arr[mid] + target < 0:
        search(mid + 1, right, target)
    else:
        search(left, mid - 1, target)


for i in arr:
    search(0, N-1, i)
ans.sort()
print(ans[0], ans[1])