from collections import deque
def solution(sequence):
    answer = 0
    e_list = list(enumerate(sequence))
    seq1 = list(map(lambda pair: pair[1] if pair[0] % 2 != 0 else pair[1] * -1, e_list))
    seq2 = list(map(lambda pair: pair[1] if pair[0] % 2 == 0 else pair[1] * -1, e_list))

    dq = deque()
    curSum = 0
    for i in seq1:
        while dq and curSum < 0:
            curSum -= dq.popleft()
        curSum += i
        answer = max(answer, curSum)
        dq.append(i)

    dq.clear()
    curSum = 0
    for i in seq2:
        while dq and curSum < 0:
            curSum -= dq.popleft()
        curSum += i
        answer = max(answer, curSum)
        dq.append(i)

    return answer
