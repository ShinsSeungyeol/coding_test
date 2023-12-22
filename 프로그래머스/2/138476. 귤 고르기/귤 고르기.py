def solution(k, tangerine):
    answer = 0
    dict_num_tangerine = {}
    
    for t in tangerine:
        if t not in dict_num_tangerine:
            dict_num_tangerine[t] = 1
        else:
            dict_num_tangerine[t] += 1
            
    
    list_num_tangerine = sorted(dict_num_tangerine.items(), key=lambda x : x[1], reverse=True)
    
    sold_num = 0;
    
    for i in range (len(list_num_tangerine)):
        if sold_num >= k:
            break
        sold_num += list_num_tangerine[i][1]
        answer += 1
    
    return answer