import sys

# input = sys.stdin.readline
# print = sys.stdout.write
N = int(input().rstrip())
arr1 = list(map(int, input().rstrip().split()))

M = int(input().rstrip())
arr2 = list(map(int, input().rstrip().split()))

arr1.sort()

global isFind
isFind = False


# 이분 탐색 구현
def search(left, right, target):
    if left > right:
        return 0
    mid = (left + right) // 2
    if arr1[mid] == target:
        return 1

    if arr1[mid] > target:
        return search(left, mid - 1, target)
    else:
        return search(mid + 1, right, target)


for i in arr2:
    print(search(0, len(arr1) - 1, i))
