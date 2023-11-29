def solution(keymap, targets):
    answer = []
    
    for target in targets:
        n_press = 0
        for c in target:
            min_press = 101
            for key in keymap:
                if (key.find(c) == -1):
                    continue
                min_press = min(min_press, key.find(c) + 1)
                
            if (min_press == 101):
                n_press = -1
                break
                
            else:
                n_press += min_press
   
        answer.append(n_press)
    return answer