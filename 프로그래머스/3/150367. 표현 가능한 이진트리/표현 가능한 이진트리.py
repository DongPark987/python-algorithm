import math

def solution(numbers):
    answer = []
    for i in numbers:
        b_num = list(map(int, bin(i)[2:]))
        perfect_len = 2 ** math.ceil(math.log2(len(b_num)+1)) - 1
        need_extend = perfect_len - len(b_num)
        b_num = [0 for _ in range(need_extend)] + b_num
        def check(bin_num):
            root = len(bin_num) // 2
            if root == 0:
                return True
            if bin_num[root] == 0:
                if 1 not in bin_num:
                    return True
                return False
            return check(bin_num[:root]) and check(bin_num[root + 1:])
        answer.append(1 if check(b_num) else 0)

    return answer