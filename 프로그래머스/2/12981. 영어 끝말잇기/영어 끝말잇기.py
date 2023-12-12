def solution(n, words):
    answer = []

    dict_v = {};
    dict_v[hash(words[0])] = 0;
    last_word = words[0]
    
    for i in range(1, len(words)):
        hash_v = hash(words[i]);
     
        if hash_v in dict_v or last_word[-1] != words[i][0]:
            answer = [(i % n) + 1, (i//n) + 1];
            break;
            
        dict_v[hash_v] = 0; 
        last_word = words[i];
    
    else: 
        answer = [0, 0]
            
    
    return answer