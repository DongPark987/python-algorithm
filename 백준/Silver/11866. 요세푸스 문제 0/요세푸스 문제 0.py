from collections import deque

N, K = map(int, input().split())

myDeque = deque([i for i in range(1, N + 1)])

ans = ['<']
while not len(myDeque) == 0:
    myDeque.rotate(-(K - 1))
    ans.append(str(myDeque[0]))
    ans.append(", ")
    myDeque.popleft()

ans[-1] = ">"
print(''.join(ans))