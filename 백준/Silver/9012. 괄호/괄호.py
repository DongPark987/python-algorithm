import sys

input = sys.stdin.readline

N = int(input())
for _ in range(N):
    myStack = []
    myStr = input().rstrip()
    isTrue = "YES"
    for i in myStr:
        if i == '(':
            myStack.append(1)
        else:
            if len(myStack) == 0:
                isTrue = "NO"
                break
            else:
                myStack.pop()
    if len(myStack) != 0:
        print("NO")
        continue
    else:
        print(isTrue)
