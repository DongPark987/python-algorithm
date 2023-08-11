def rec2(N, From, via, to):
    global n
    global ans
    if N == 1:
        print(From, to)
        return
    rec2(N - 1, From, to, via)
    print(From, to)
    rec2(N - 1, via, From, to)


global ans
ans = 0
global n
n = int(input())

print(2 ** n - 1)
if (n <= 20):
    rec2(n, 1, 2, 3)
