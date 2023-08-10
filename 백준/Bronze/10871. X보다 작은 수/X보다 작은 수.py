N, x = map(int, input().split())

str = list(input().split())

for i in range(N):
    if int(str[i])<x:
        print(str[i])