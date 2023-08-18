import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
arr = list(map(int, input().split()))
myStack = []
ans = arr

for i in range(N, 0, -1):
    if myStack:
        while myStack:
            if arr[i - 1] >= arr[myStack[-1]]:
                ans[myStack[-1]] = i
                # print(str(i) + ' ')
                myStack.pop()
            else:
                break
    myStack.append(i - 1)

while myStack:
    ans[myStack[-1]] = 0
    # print(str(0) + ' ')
    myStack.pop()

for i in ans:
    print(str(i) + " ")
