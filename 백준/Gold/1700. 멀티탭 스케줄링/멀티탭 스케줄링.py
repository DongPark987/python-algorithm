from heapq import heappush, heappop
from collections import deque

N, K = map(int, input().split())
arr = list(map(int, input().split()))

# print(arr)

schedule = [deque() for _ in range(K + 1)]

for i in range(K):
    schedule[arr[i]].append(i + 1)
for i in range(K + 1):
    schedule[i].append(999999)

ans = 0
useCnt = 0
isPlugIn = [False] * (K + 1)
mySet = set()
for curPlug in arr:
    schedule[curPlug].popleft()
    # print(curPlug, schedule)
    # 여유 콘센트가 있을때
    if useCnt < N:
        isPlugIn[curPlug] = True
        if curPlug not in mySet:
            useCnt += 1
            mySet.add(curPlug)
    else:
        if curPlug in mySet:
            continue
        else:
            # 뽑을거 찾기
            Max = 0
            pick = 0
            for i in mySet:
                # print(i)
                # print(schedule)
                if schedule[i][0] > Max:
                    pick = i
                    Max = schedule[i][0]
            mySet.remove(pick)
            mySet.add(curPlug)
            ans += 1

print(ans)