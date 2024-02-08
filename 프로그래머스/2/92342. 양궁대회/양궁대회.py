def solution(n, info):
    answer = [-1]
    Max = 0
    Max_2 = 1000
    lion = [0 for _ in range(11)]

    def dfs(loc, l, r):
        nonlocal Max, Max_2, answer, n
        if loc == 11:
            if Max < l - r :
                answer = lion[:]
                answer[10] += n
                Max = l - r
                Max_2 = l
            elif Max == l-r:
                if Max_2 <= l:
                    answer = lion[:]
                    answer[10] += n
                    Max = l - r
                    Max_2 = l
            return

        # 승
        if info[loc] < n:
            lion[loc] = info[loc] + 1
            n -= info[loc] + 1
            dfs(loc + 1, l + 10 - loc, r)
            lion[loc] = 0
            n += info[loc] + 1
        # 패
        if info[loc] != 0:
            dfs(loc + 1, l, r + 10 - loc)
        else:
            dfs(loc + 1, l, r)

    dfs(0, 0, 0)
    return answer