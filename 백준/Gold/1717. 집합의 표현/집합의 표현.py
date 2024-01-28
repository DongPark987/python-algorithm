import sys

N, M = map(int, sys.stdin.readline().split())

parent = [i for i in range(N + 1)]

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def is_union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return True
    else:
        return False


def merge(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    parent[y] = x


for _ in range(M):
    op, a, b = map(int, sys.stdin.readline().split())
    if op == 0:
        merge(a,b)
    else:
        if is_union(a,b):
            print("YES")
        else:
            print("NO")