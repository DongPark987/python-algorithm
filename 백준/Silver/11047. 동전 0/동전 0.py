N, K = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.reverse()

ans = 0
for i in arr:
    cnt = K // i
    K -= i * cnt
    ans += cnt
print(ans)