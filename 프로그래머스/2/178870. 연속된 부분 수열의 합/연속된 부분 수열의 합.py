from collections import deque
def solution(sequence, k):
    answer = [-1000000,1000000]
    q = deque()
    sum = 0
    for i in range(len(sequence)):
        q.append(i)
        sum+=sequence[i]
        while q and sum > k:
            sum -= sequence[q.popleft()]
        if sum == k:
            if (answer[1] - answer[0]) > (q[-1]-q[0]):
                answer = [q[0],q[-1]]

    return answer