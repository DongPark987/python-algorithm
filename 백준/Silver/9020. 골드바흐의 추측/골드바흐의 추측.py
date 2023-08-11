dnum = [True for i in range(10002)]

for i in range(2, 200):
    if dnum[i]:
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
    b = 100000
    for j in range(n):
        if j >= n:
            break
        if dnum[j]:
            if dnum[n - j]:
                if abs(a - b) > abs(j * 2 - n):
                    a = j
                    b = n - j
    print(a, b)
