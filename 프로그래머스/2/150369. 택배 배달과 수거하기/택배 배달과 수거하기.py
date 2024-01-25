def solution(cap, n, deliveries, pickups):
    answer = 0
    d_idx = n
    p_idx = n
    while True:
        tmpCap = cap
        curr = -1
        for idx in range(d_idx - 1, -1, -1):
            if deliveries[idx] != 0:
                curr = max(curr, idx + 1)
                tmpCap -= deliveries[idx]
                if tmpCap <= 0:
                    deliveries[idx] = -tmpCap
                    break
                else:
                    deliveries[idx] = 0
        d_idx = curr
        tmpCap = cap
        curr = -1
        for idx in range(p_idx - 1, -1, -1):
            if pickups[idx] != 0:
                curr = max(curr, idx + 1)
                tmpCap -= pickups[idx]
                if tmpCap <= 0:
                    pickups[idx] = -tmpCap
                    break
                else:
                    pickups[idx] = 0
        p_idx = curr
        curr = max(p_idx, d_idx)
        if curr == -1:
            break
        answer += (curr * 2)


    return answer