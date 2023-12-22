def solution(elements):
    answer = 0
    possible_num = set()
    size = len(elements)
    
    for i in range(size):
        num = 0
        for j in range(size):
            num += elements[(i+j) % size]
            possible_num.add(num)
            
            
    return len(possible_num)
                
                
    
    
    
    return answer