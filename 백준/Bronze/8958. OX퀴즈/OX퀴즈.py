n = int(input())
myStr = []
for i in range(n):
    myStr.append(input())

for i in range(n):
    cnt = 1
    ans = 0
    for s in myStr[i]:
        if s == 'O':
            ans += cnt
            cnt+=1
        else:
            cnt = 1
    print(ans)

