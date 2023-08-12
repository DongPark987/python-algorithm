from itertools import combinations
import sys
input = sys.stdin.readline
print = sys.stdout.write

arr = []
ans = []
for _ in range(9):
    arr.append(int(input().rstrip()))

for i in combinations(arr, 7):
    if sum(i) == 100:
        ans = list(i)

ans.sort()
for i in ans:
    print(str(i) + '\n')
