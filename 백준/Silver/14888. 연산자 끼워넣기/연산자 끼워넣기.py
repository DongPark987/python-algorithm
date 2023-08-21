import math

N = input()

arr = list(map(int, input().split()))
operator = list(map(int, input().split()))

# print(arr)
# print(operator)

Max = -math.inf
Min = math.inf
end = len(arr)


def rec(loc, Sum):
    global end, Max, Min, operator
    if loc == end:
        Max = max(Max, Sum)
        Min = min(Min, Sum)
        return

    if operator[0] != 0:
        operator[0] -= 1
        rec(loc + 1, Sum + arr[loc])
        operator[0] += 1

    if operator[1] != 0:
        operator[1] -= 1
        rec(loc + 1, Sum - arr[loc])
        operator[1] += 1

    if operator[2] != 0:
        operator[2] -= 1
        rec(loc + 1, Sum * arr[loc])
        operator[2] += 1

    if operator[3] != 0:
        operator[3] -= 1
        if Sum < 0:
            rec(loc + 1, -(abs(Sum) // arr[loc]))
        else:
            rec(loc + 1, Sum // arr[loc])
        operator[3] += 1


rec(1, arr[0])
print(Max)
print(Min)
