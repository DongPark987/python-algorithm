import re

N = input()

operator = ["+", ]
for i in list(N):
    if i == '+' or i == '-':
        operator.append(i)

N = list(map(int, re.split("[+ | -]", N)))

Plus = 0
Minus = 0
isMinus = False
for idx in range(len(N)):
    if operator[idx] == "-":
        isMinus = True
    if isMinus:
        Minus += N[idx]
    else:
        Plus += N[idx]
print(Plus - Minus)
