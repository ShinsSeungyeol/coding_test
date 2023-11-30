def solution(number, limit, power):
    
    measure = [0 for i in range(number+1)]
    
    measure[0] = 0
    measure[1] = 1
    answer = 1
    
    for i in range(2, number+1):
        for j in range(1, int(i ** 0.5)+1):
            if (i % j == 0):
                measure[i] += 2
        else:
            if i == int(i ** 0.5) * int(i ** 0.5):
                measure[i] -= 1
                
        if measure[i] > limit:
            answer += power
        else:
            answer += measure[i]
            
    return answer
            
    