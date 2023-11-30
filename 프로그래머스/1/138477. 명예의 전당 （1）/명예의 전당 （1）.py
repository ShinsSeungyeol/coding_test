def solution(k, score):
    answer = []
    sorted_score = []
    for i in range(1, len(score) + 1):
        sorted_score = sorted(score[0:i])
        
        if i <= k:
            answer.append(sorted_score[0])
        else:
            answer.append(sorted_score[i-k])
        
    
        
    return answer
