import sys
import bisect

input = sys.stdin.readline

N, M = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = [list(map(int, input().split())) for _ in range(M)]

arr1.sort()

for i in arr2:
    left = bisect.bisect_left(arr1, i[0])
    right = bisect.bisect_right(arr1, i[1])
    print(right - left)
