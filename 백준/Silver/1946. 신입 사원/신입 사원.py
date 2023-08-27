import sys

input = sys.stdin.readline


def sol():
    N = int(input())

    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    arr.sort(key=lambda x: (x[0], x[1]))

    Min = arr[0][1]
    ans = 0
    for i in arr:
        if Min < i[1]:
            ans += 1
        else:
            Min = i[1]
    print(N - ans)


K = int(input())
for _ in range(K):
    sol()
