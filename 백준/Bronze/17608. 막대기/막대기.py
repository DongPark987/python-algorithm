import sys

input = sys.stdin.readline

N = int(input())

myStack = []

for _ in range(N):
    myStack.append(int(input()))

ans = 1
Max = myStack[-1]
myStack.pop()
while len(myStack) != 0:
    if Max >= myStack[-1]:
        myStack.pop()
    else:
        Max = myStack[-1]
        ans += 1
        myStack.pop()
print(ans)