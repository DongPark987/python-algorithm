def solution(bandage, health, attacks):
    totalTime = attacks[-1][0];
    hillTime = 0;
    health2 = health
    for i in range(0,totalTime+1):
        if i == attacks[0][0]:
            health2 -= attacks[0][1]
            hillTime = 0
            if health2 <= 0:
                return -1
            attacks.pop(0)
            continue
        hillTime += 1
        health2 += bandage[1]
        if hillTime == bandage[0]:
            health2 += bandage[2]
            hillTime = 0
        if health2 > health:
            health2 = health
            
    return health2