import math
from collections import deque


def solution(queue1, queue2):
    ans = 0
    dq1 = deque(queue1)
    dq2 = deque(queue2)
    dq1_sum = sum(queue1)
    dq2_sum = sum(queue2)
    max_try = (len(queue1) + len(queue2)) * 4

    while dq1_sum != dq2_sum:
        ans += 1
        if ans > max_try:
            return -1
        if dq1_sum > dq2_sum:
            tmp = dq1.popleft()
            dq1_sum -= tmp
            dq2.append(tmp)
            dq2_sum += tmp
        else:
            tmp = dq2.popleft()
            dq2_sum -= tmp
            dq1.append(tmp)
            dq1_sum += tmp

    return ans