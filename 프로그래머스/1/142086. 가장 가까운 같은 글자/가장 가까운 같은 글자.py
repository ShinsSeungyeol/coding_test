def solution(s):
    answer = [-1 for i in range(len(s))]
    
    for i in range(1, len(s)):
        if s[0: i].rfind(s[i]) != -1:
            answer[i] = i - s[0: i].rfind(s[i]);
    

    
    return answer