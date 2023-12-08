import math
def solution(n):
    answer = 1
    
    for i in range(1, n//2 + 1):
        answer += math.comb(n-i, i)
        answer %= 1234567
    return answer