N = int(input())

a = 1
b = 2
c = 0

for i in range(2, N):
    c = (a + b) % 15746
    a = b
    b = c

if N == 1:
    print(a)
elif N == 2:
    print(b)
else:
    print(c)
