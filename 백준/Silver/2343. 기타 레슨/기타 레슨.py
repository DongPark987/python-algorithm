import sys

N, M = map(int, sys.stdin.readline().split())
lesson = list(map(int, sys.stdin.readline().split()))

def solve():

    left, right = max(lesson), sum(lesson)
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        cnt = 1
        size = 0
        for i in lesson:
            if size + i > mid:
                size = i
                cnt += 1
            else:
                size += i
        if cnt > M:
            left = mid + 1
        else:
            right = mid - 1
            ans = mid
    print(ans)


solve()