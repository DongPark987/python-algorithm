n = input()

cnt = 10
if int(n) <= 10:
    print(n)
    exit()
for i in range(11, int(n) + 1):
    nList = list(map(int, list(str(i))))
    # print(nList)
    interval = nList[1] - nList[0]
    tf = True
    for j in range(len(nList) - 1):
        if nList[j] + interval != nList[j + 1]:
            # print(f'a{interval}aaa{nList[0], nList[1]}')
            tf = False
    if tf:
        cnt += 1

print(cnt)
