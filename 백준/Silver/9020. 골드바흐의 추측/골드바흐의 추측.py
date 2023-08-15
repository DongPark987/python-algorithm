dnum = [True for i in range(10002)]
dnumList = []

# 에라토스테네스의 체를 이용한 소수 배열 구하기
for i in range(2, 10001):
    if dnum[i]:
        dnumList.append(i)
        cnt = 2
        while (True):
            tmp = i * cnt
            if tmp <= 10001:
                dnum[tmp] = False
                cnt += 1
            else:
                break

T = int(input())
for i in range(T):
    n = int(input())
    a = 0
    b = 1000001
    for j in dnumList:
        if j > n - j:
            break
        if dnum[n - j]:
            if abs(a - b) > abs(j - (n - j)):
                a = j
            b = n - j
    print(a, b)
