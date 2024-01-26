from collections import deque
import math


def solution(m, n, startX, startY, balls):
    answer = []

    for ball in balls:
        x = ball[0]
        y = ball[1]
        Min = 999999

        # 좌
        if not (startY == y and startX > x):
            Min = min(Min, (startX + x) ** 2 + (startY - y) ** 2)

        # 우
        if not (startY == y and startX < x):
            Min = min(Min, (2 * m - startX - x) ** 2 + (startY - y) ** 2)

        # 상
        if not (startX == x and startY < y):
            Min = min(Min, (startX - x) ** 2 + (2 * n - startY - y) ** 2)

        # 하
        if not (startX == x and startY > y):
            Min = min(Min, (startX - x) ** 2 + (startY + y) ** 2)

        answer.append(Min)

    return answer