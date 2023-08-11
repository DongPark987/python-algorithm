import sys

input = sys.stdin.readline
n = int(input())
data = []
for i in range(n):
    data.append(input().rstrip())
for i in data:
    j = i.split(' ')
    for k in list(j[1]):
        print(k * int(j[0]), end="")
    print()
