import sys


input = sys.stdin.readline
global L
M, N, L = map(int, input().split())

global hunter, animal, ans
hunter = []
animal = []
ans = 0

hunter = list(map(int, input().split()))
hunter.sort()
for _ in range(N):
    animal.append(list(map(int, input().split())))


# print(animal)
# print(hunter)

def search(left, right, x, y):
    if (left > right):
        return
    global ans, hunter, animal, L
    mid = (left + right) // 2
    distance = abs(hunter[mid] - x) + y
    if (distance <= L):
        ans += 1
        return
    else:
        if x < hunter[mid]:
            search(left, mid - 1, x, y)
        elif x > hunter[mid]:
            search(mid + 1, right, x, y)
        else:
            return


for i in animal:
    search(0, M, i[0], i[1])
print(ans)
