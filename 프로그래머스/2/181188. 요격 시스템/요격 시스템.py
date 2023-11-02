def solution(targets):
    answer = 1
    targets.sort(key = lambda x: (x[1], x[0]))
    # print(targets)
    curr_explosion = targets[0][1]-0.5
    for i in range(1, len(targets)):
        # print(curr_explosion,targets[i][0])
        if curr_explosion < targets[i][0]:
            curr_explosion = targets[i][1]-0.5
            answer += 1
    return answer