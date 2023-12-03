def solution(survey, choices):
    answer = ''
    
    score = {c:0 for c in (['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N' ])}
    
    dir = [[0, 0], [0, 3], [0, 2], [0, 1], [0, 0], [1, 1], [1, 2], [1, 3]]
    
    for i, c in enumerate(choices):
        score[survey[i][dir[c][0]]] += dir[c][1]

            
    for type in ['RT', 'CF', 'JM', 'AN']:
        answer += type[0] if score[type[0]] >= score[type[1]] else type[1]
    
    return answer