import sys
import math

input = sys.stdin.readline
# print = sys.stdout.write

V, E = map(int, input().split())

arr = []
parent = [i for i in range(V + 1)]

for _ in range(E):
    a, b, c = list(map(int, input().split()))
    arr.append((a - 1, b - 1, c))

arr.sort(key=lambda x: x[2])


def findParent(cursor):
    global parent
    if parent[cursor] == cursor:
        return cursor
    else:
        return findParent(parent[cursor])


def unionParent(A, B):
    global parent
    A = findParent(A)
    B = findParent(B)
    if A <= B:
        parent[B] = A
    else:
        parent[A] = B


ans = 0
for edge in arr:
    if findParent(edge[0]) != findParent(edge[1]):
        unionParent(edge[0], edge[1])
        ans += edge[2]
print(ans)
