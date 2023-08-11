dnum = [True for i in range(1001)]

for i in range(2, 40):
    if dnum[i]:
        cnt = 2
        while (True):
            tmp = i * cnt
            if tmp <= 1000:
                dnum[tmp] = False
                cnt+=1
            else:
                break
dnum[1] = False
dnum[0] = False

input()
n = list(map(int, input().split()))

cnt = 0;
for i in n:
    if(dnum[i]):
        cnt+=1

print(cnt)
