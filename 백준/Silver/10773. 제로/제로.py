import sys

input = sys.stdin.readline

myStack = []

N = int(input())

for _ in range(N):
    tmp = int(input())
    if tmp !=0:
        myStack.append(tmp)
    else:
        myStack.pop()

print(sum(myStack))