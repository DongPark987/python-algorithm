import sys
from collections import deque

# input = sys.stdin.readline


data = list(input())

myStack = []

for i in data:
    myStack.append(i)
    if len(myStack) >= 4 and "".join(myStack[-4:]) == "PPAP":
        for _ in range(3): myStack.pop()

if len(myStack) == 1 and myStack[0] == 'P':
    print("PPAP")
else:
    print("NP")
