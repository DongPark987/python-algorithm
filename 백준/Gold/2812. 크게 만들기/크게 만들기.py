import sys

print = sys.stdout.write

N, K = map(int, input().split())

# a = [input()]
# print(a)
arr = list(map(int, list(input())))

myStack = []
cnt = 0

myStack.append(arr[0])
for i in range(1, N):
    if len(myStack) != 0 or myStack[-1] < arr[i]:
        while cnt < K:
            if len(myStack) == 0 or myStack[-1] >= arr[i]:
                break
            myStack.pop()
            cnt += 1
        myStack.append(arr[i])
    else:
        myStack.append(arr[i])

for i in range(0, len(myStack) - (K - cnt)):
    print(str(myStack[i]))
