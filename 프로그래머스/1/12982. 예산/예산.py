def solution(d, budget):
    answer = 0
    d = sorted(d)
    
    sum = 0
    
    for i, val in enumerate(d):
        sum += val
        
        if sum > budget:
            break        
        answer += 1
    return answer