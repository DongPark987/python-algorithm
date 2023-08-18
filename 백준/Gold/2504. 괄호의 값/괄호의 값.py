myStr = input().rstrip()

ans = 0
N = 1
myStack = []
for i in range(len(myStr)):
    # print(myStack)
    # print(ans)
    if myStr[i] == "(":
        N *= 2
        myStack.append(myStr[i])
        continue
    if myStr[i] == "[":
        N *= 3
        myStack.append(myStr[i])
        continue

    if myStr[i] == ")":
        if not myStack or myStack[-1] != '(':
            print(0)
            exit()
        if myStr[i-1] == '(':
            ans += N
        N //= 2
        myStack.pop()
        continue

    if myStr[i] == "]":
        if not myStack or myStack[-1] != '[':
            print(0)
            exit()
        if myStr[i - 1] == '[':
            ans += N
        N //= 3
        myStack.pop()
        continue

if not myStack:
    print(ans)
else:
    print(0)