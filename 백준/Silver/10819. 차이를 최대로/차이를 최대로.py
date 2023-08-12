from itertools import combinations, permutations
import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
ans = -10000

for i in permutations(arr, N):
    mySum = 0
    for j in range(len(i)-1):
        mySum += abs(i[j]-i[j+1])
    ans = max(mySum, ans)


print(str(ans))
