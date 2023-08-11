N = int(input())

arr = []

for _ in range(N):
    arr.append(int(input()))

for i in range(N-1):
    for j in range(i, N):
        if arr[i] >= arr[j]:
            tmp = arr[j]
            arr[j] = arr[i]
            arr[i] = tmp

for i in arr:
    print(i)