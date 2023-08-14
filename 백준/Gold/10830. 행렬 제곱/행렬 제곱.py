import sys

input = sys.stdin.readline

A, B = map(int, input().split())

global arr
arr = []

for _ in range(A):
    arr.append(list(map(int, input().split())))


def matMulti(arr1, arr2):
    multi = []
    vArr = []
    for i in range(A):
        tmp = []
        for j in range(A):
            tmp.append(arr2[j][i])
        vArr.append(tmp)
    for i in range(A):
        tmp = []
        for j in range(A):
            tmp.append(sum(list(map(lambda x, y: x * y, arr1[i], vArr[j]))))
        multi.append(tmp)
    return multi


def matMod(arr):
    for i in range(A):
        for j in range(A):
            arr[i][j] %= 1000
    return arr


def rec(B):
    global arr
    if B == 1:
        return matMod(arr)

    k = matMod(rec(B // 2))

    if B % 2 == 0:
        return matMod(matMulti(k, k))
    else:
        return matMod(matMulti(matMod(matMulti(k, k)), arr))


ans = rec(B)

for i in range(A):
    for j in range(A):
        print(ans[i][j], end=" ")
    print()
