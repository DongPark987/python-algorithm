from itertools import combinations
import sys
input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))

ans = 1000000
Result = 0

for i in combinations(arr, 3):
    mySum = sum(i)
    # print(str(mySum)+'\n')
    if mySum <= M:
        if M-mySum < ans:
            Result = mySum
            ans = M-mySum

print(str(Result))
