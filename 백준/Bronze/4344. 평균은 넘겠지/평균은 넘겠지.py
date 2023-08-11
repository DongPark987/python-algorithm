n = int(input())
score = []
for i in range(n):
    score.append(list(map(int, input().split())))
    score[i].pop(0)
ans = []
for i in score:
    avg = 0
    for j in i:
        avg += j
    avg = avg / len(i)
    cnt = 0
    for j in i:
        if j > avg:
            cnt += 1
    ans.append(cnt / len(i) * 100)
for i in ans:
    print(f'{round(i, 3)}%')