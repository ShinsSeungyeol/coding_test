def solution(cards1, cards2, goal):
    answer = ''
    
    for word in goal:
        if len(cards1) > 0 and cards1[0] == word:
            cards1 = cards1[1:]
        elif len(cards2) > 0 and cards2[0] == word:
            cards2 = cards2[1:]
        else:
            answer = 'No'
            break;
    else:
        answer = 'Yes'
            
    return answer