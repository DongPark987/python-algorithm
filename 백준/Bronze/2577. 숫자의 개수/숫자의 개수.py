n = []
for i in range(3):
    n.append(int(input()))
n2 = 1
for i in n:
    n2 *= i

n3 = list(str(n2))
ans = [0 for i in range(10)]
for i in n3:
    ans[int(i)] += 1

for i in ans:
    print(i)
