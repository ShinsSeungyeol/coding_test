def solution(n, lost, reserve):
    cmm = [l for l in lost if l in reserve]
    lost = sorted([l for l in lost if l not in cmm])
    reserve = sorted([r for r in reserve if r not in cmm])
    
    answer = n - len(lost)
    for i, r in enumerate(reserve):
        possible_list = [l for l in lost if r-1 == l or r+1 ==l]
        
        
        if len(possible_list) >= 1:
            answer += 1
            lost.remove(possible_list[0])
        
        
        
    return answer