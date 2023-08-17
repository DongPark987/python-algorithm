import sys

input = sys.stdin.readline

myStack = []


def myPush(data):
    global myStack
    # print("추가", data)
    myStack.append(data)
    pass


def myPop():
    global myStack
    if len(myStack) == 0:
        return -1
    return myStack.pop()
    pass


def mySize():
    global myStack
    return len(myStack)
    pass


def myEmpty():
    global myStack
    if len(myStack) == 0:
        return 1
    else:
        return 0
    pass


def myTop():
    global myStack
    if len(myStack)==0:
        return -1
    else:
        return myStack[-1]
    pass


N = int(input().rstrip())

for _ in range(N):
    myStr = list(input().rstrip().split())
    # print(myStr)
    if myStr[0] == "push":
        myPush(myStr[1])
        pass
    elif myStr[0] == "pop":
        print(myPop())
        pass
    elif myStr[0] == "size":
        print(mySize())
        pass
    elif myStr[0] == "empty":
        print(myEmpty())
        pass
    elif myStr[0] == "top":
        print(myTop())
        pass
