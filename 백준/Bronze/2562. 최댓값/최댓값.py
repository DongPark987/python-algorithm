n = list()
for i in range(9):
    n.append(int(input()))

result = [0, 0]
for i in range(9):
    if n[i] > result[0]:
        result = [n[i], i+1]
for i in result:
    print(i)
