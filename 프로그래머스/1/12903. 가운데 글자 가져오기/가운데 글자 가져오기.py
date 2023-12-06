def solution(s):
    size = len(s)
    
    if size % 2 == 0:
        return s[size//2-1:size//2+1]
    else:
        return s[size//2]