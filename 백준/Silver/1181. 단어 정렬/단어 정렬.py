import sys
input = sys.stdin.readline
print = sys.stdout.write


n = int(input().rstrip())
myStr = set()
for _ in range(n):
    myStr.add(input().rstrip())

myTuple = []
for (i, j) in zip(myStr, list(map(len, myStr))):
    myTuple.append((j, i))
myTuple.sort(key=lambda x: (x[0], x[1]))

for i in myTuple:
    print(i[1]+"\n")
