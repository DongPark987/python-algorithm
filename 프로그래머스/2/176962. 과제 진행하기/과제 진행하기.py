def solution(plans):
    answer = []
    stack = []
    plans.sort(key=lambda x: x[1])
    for work in plans:
        time = work[1].split(':')
        work[1] = int(time[0]) * 60 + int(time[1])
        work[2] = int(work[2])

    next_idx = 0
    current_work = None
    for time in range(24 * 60):

        if plans[next_idx][1] == time:
            if current_work:
                current_work[2] -= 1
                if current_work[2] == 0:
                    answer.append(current_work[0])
                else:
                    stack.append([current_work[0], current_work[2]])
            else:
                if stack:
                    top = stack[-1]
                    top[1] -= 1
                    if top[1] == 0:
                        answer.append(stack.pop()[0])

            current_work = plans[next_idx]
            next_idx += 1
            if next_idx == len(plans):
                break
            continue

        if current_work:
            current_work[2] -= 1
            if current_work[2] == 0:
                answer.append(current_work[0])
                current_work = None
        else:
            if stack:
                top = stack[-1]
                top[1] -= 1
                if top[1] == 0:
                    answer.append(stack.pop()[0])
    answer.append(plans[-1][0])
    while stack:
        answer.append(stack.pop()[0])
    return answer