N = int(input())

global ans
ans = 0
col = [0 for i in range(15)]


def check(y):
    for i in range(y):
        if col[i] == col[y] or abs(col[i] - col[y]) == abs(i - y):
            return False
    return True


def rec(loc):
    global ans
    if loc == N:
        ans += 1
        return
    else:
        for i in range(N):
            col[loc] = i
            if check(loc):
                rec(loc + 1)
rec(0)
print(ans)
