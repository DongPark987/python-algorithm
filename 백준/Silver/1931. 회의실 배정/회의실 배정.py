import sys
input = sys.stdin.readline
N = int(input())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: (x[0], x[1]))

# for i in range(N):
#     print(arr[i])

cur = arr[0]
ans = 1
for i in range(1, len(arr)):
    if cur[1] <= arr[i][0]:
        ans += 1
        cur = arr[i]
    else:
        if cur[1] > arr[i][1]:
            cur = arr[i]
print(ans)

