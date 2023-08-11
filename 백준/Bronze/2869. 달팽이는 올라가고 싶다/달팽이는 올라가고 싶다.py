import math

a, b, v = map(int, input().split())

oneDay = a - b
day = math.ceil(v / oneDay)

if (v - b) % (a - b) == 0:
    print((v - b) // (a - b))
else:
    print((v - b) // (a - b) + 1)
