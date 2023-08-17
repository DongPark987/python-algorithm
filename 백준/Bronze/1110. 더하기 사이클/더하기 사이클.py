n1 = input()
n2 = n1
cnt = 0

while True:
    if int(n2) < 10:
        n2 = "0" + n2
    # print(n2)
    cnt+=1
    a = list(n2)
    a_sum = str(int(a[0]) + int(a[1]))
    a_sum_last = list(a_sum)[-1]
    n2 = str(int(a[1])*10 + int(a_sum_last))
    if n1 == n2:
        break
print(cnt)
