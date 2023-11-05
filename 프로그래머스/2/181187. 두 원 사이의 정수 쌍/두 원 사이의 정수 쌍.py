import math
def solution(r1, r2):
    answer = 0
    
    r1_dot = 0
    for i in range(1,r1+1):
        if int(math.sqrt(r1**2-i**2)) == math.sqrt(r1**2-i**2):
            # print(int(math.sqrt(r1**2-i**2)), math.sqrt(r1**2-i**2))
            r1_dot += int(math.sqrt(r1**2-i**2))
        else:
            r1_dot += int(math.sqrt(r1**2-i**2))+1
    # print(r1_dot)
        
    r2_dot = 0
    for i in range(1,r2+1):
        r2_dot += int(math.sqrt(r2**2-i**2))+1
    # print(r2_dot)
    return ((r2_dot-r1_dot))*4
    
    
    
    return answer