def solution(lottos, win_nums):
    answer = []
    scribbling = len([i for i in lottos if i == 0])
    match = 0
    
    for i in lottos:
        if i in win_nums:
            match += 1
            
    ranking = [6, 6, 5, 4, 3, 2, 1]
    
    answer = [ranking[match + scribbling], ranking[match]]
        
    return answer