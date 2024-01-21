from heapq import heappop, heappush


def solution(book_time):
    for i in book_time:
        tmp = i[0].split(':')
        tmp[0] = int(tmp[0]) * 60
        i[0] = tmp[0] + int(tmp[1])
        tmp = i[1].split(':')
        tmp[0] = int(tmp[0]) * 60
        i[1] = tmp[0] + int(tmp[1]) + 10
    book_time.sort(key=lambda x: (x[0], x[1]))
    answer = 0
    curRoomCnt = 0
    hq = []
    for book in book_time:
        if hq:
            while hq and hq[0] <= book[0]:
                heappop(hq)
                curRoomCnt -= 1
        heappush(hq, book[1])
        curRoomCnt += 1
        answer = max(answer, curRoomCnt)
    return answer
