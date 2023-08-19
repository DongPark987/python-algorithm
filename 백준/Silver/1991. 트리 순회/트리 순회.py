import sys

input = sys.stdin.readline

myDic = {}

N = int(input())


def circuit(node, type):
    if node == '.':
        return
    if type == 0:
        print(node, end="")
    circuit(myDic[node][0], type)
    if type == 1:
        print(node, end="")
    circuit(myDic[node][1], type)
    if type == 2:
        print(node, end="")


for _ in range(N):
    a, b, c = input().split()
    myDic[a] = [b, c]

for i in range(3):
    circuit('A', i)
    print()
