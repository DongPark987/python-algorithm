from itertools import combinations, permutations
import sys
input = sys.stdin.readline
# print = sys.stdout.write
N = int(input().rstrip())

arr = list(map(int, input().rstrip().split()))
arr2 = list(map(int, input().rstrip().split()))
minAns = 100000000000
maxAns = -100000000000

operList = []
for i in range(len(arr2)):
    for j in range(arr2[i]):
        operList.append(i)

# print(operList)
for operList in permutations(operList, N-1):
    mySum = arr[0]
    for j in range(1, N):
        if operList[j-1] == 0:
            mySum += arr[j]
        elif operList[j-1] == 1:
            mySum -= arr[j]
        elif operList[j-1] == 2:
            mySum *= arr[j]
        elif operList[j-1] == 3:
            if (mySum < 0):
                mySum = -(abs(mySum)//arr[j])
            else:
                mySum //= arr[j]
    minAns = min(minAns, mySum)
    maxAns = max(maxAns, mySum)

print(maxAns)
print(minAns)
