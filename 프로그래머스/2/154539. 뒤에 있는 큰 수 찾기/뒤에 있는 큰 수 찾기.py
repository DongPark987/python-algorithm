def solution(numbers):
    answer = [0 for _ in range(len(numbers))]
    stack = []

    for i in range(len(numbers) - 1, -1, -1):
        while stack and stack[-1] <= numbers[i]:
            stack.pop()
        if not stack:
            answer[i] = -1
        else:
            answer[i] = stack[-1]
        stack.append(numbers[i])

    return answer