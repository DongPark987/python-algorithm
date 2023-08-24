N = int(input())

arr = [0] * 101
arr[0] = 0
arr[1] = 1

for i in range(2, 101):
    arr[i] = arr[i - 1] + arr[i - 2]

print(arr[N])
