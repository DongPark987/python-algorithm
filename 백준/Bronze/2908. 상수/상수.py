import functools

a, b = input().split()
a = list(a)
b = list(b)
a.reverse()
b.reverse()
a = functools.reduce(lambda x, y: 10 * x + y, map(int, a), 0)
b = functools.reduce(lambda x, y: 10 * x + y, map(int, b), 0)

print(max(a,b))
