def solution(babbling):
    answer = 0
    
    for s in babbling:
        can = ['aya', 'ye', 'woo', 'ma']
        
        i = 0;
        before_say = ''
        
        while i < len(s):
            if s[i: i+2] in can and before_say != s[i: i+2] :
                before_say = s[i: i+2]
                i+=2
            elif s[i: i+3] in can and before_say != s[i: i+3]: 
                before_say  = s[i: i+3]
                i+=3
            else:
                break
        if i >= len(s):
            answer += 1
                
            
            
            
        
        
    return answer