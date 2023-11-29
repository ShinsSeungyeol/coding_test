def solution(n, m, section):
    answer = 0
    to_paint = section[0]
 
    for i, s in enumerate(section):
        if (to_paint > section[-1]):
            break
        if (to_paint + m <= s):
            to_paint = s
            answer += 1
    else:
        answer += 1       
        
            
        
    return answer