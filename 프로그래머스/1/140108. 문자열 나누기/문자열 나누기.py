def solution(s):
    answer = 0
    equal_cnt, diff_cnt, i = 0, 0, 0;
    basis = s[0];
    
    
    for i in range(len(s)):
        if equal_cnt == 0 and diff_cnt == 0:
            basis = s[i]
        
        if basis == s[i]:
            equal_cnt += 1
        else:
            diff_cnt += 1
        
        if equal_cnt == diff_cnt or i == len(s) - 1:
            answer += 1
            equal_cnt, diff_cnt = 0, 0
    
        
    
    
    return answer