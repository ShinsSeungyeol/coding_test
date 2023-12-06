def solution(x):
    answer = True
    
    total = sum([int(c) for c in str(x)])
    
    if x % total == 0:
        answer = True
    else:
        answer = False
    
        
    return answer