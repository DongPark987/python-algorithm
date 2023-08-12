from itertools import combinations, permutations
import sys

input = sys.stdin.readline
# print = sys.stdout.write
N = int(input().rstrip())

arr = []

global colorCnt
colorCnt = [0, 0]

for i in range(N):
    arr.append(list(map(int, input().rstrip().split())))

def rec(x, y, length):
    startColor = arr[y][x]
    if length == 1:
        colorCnt[startColor] += 1
        return
    try:
        for i in range(y, length + y):
            for j in range(x, length + x):
                if arr[i][j] != startColor:
                    raise NotImplementedError
        colorCnt[startColor] += 1
        return
    except:
        rec(x, y, length // 2)
        rec(x + length // 2, y, length // 2)
        rec(x, y + length // 2, length // 2)
        rec(x + length // 2, y + length // 2, length // 2)


rec(0, 0, N)
print(colorCnt[0],colorCnt[1])
