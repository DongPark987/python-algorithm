n = int(input())
k = int(input())
card = []
global mySet
mySet = set()
global visit


def rec(loc, sum):
    global mySet
    global visit
    if loc == k:
        mySet.add(sum)
        return
    for i in range(n):
        if not visit[i]:
            visit[i] = True
            rec(loc + 1, str(sum) + card[i])
            visit[i] = False

for _ in range(n):
    card.append(input())
visit = [False for i in range(n)]

rec(0, "")
print(len(mySet))
