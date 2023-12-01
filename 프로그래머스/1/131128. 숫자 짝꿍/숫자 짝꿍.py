def solution(X, Y):
    answer = ''
    
    d_x = { str(i):0 for i in range(10)}
    d_y = { str(i):0 for i in range(10)}
    d_common = {}
    for v in X:
        d_x[v] += 1
        
    for v in Y:
        d_y[v] += 1
        
    
    for i in range(10):
        if (d_x[str(i)] != 0 and d_y[str(i)] != 0):
            n = min(d_x[str(i)], d_y[str(i)])
            d_common[str(i)] = n
            
    if (d_common != {}):
        for i in range(9, -1, -1):
            if (str(i) in d_common):
                if (str(i) == '0' and answer == ''):
                    answer = '0'
                else:
                    answer += str(i) * d_common[str(i)]
    else:
        answer = '-1'
        
    
    return answer