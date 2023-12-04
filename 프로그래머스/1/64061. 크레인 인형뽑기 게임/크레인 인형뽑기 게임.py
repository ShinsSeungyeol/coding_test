def solution(board, moves):
    answer = 0
    basket = [];
    
    for j, value in enumerate(moves):
        doll_type = 0
        for i in range(len(board)): 
            if board[i][value-1] != 0: 
                doll_type = board[i][value-1]
                board[i][value-1] = 0
                break
        else:
            continue
                
        basket.append(doll_type)
        
        if (len(basket) >= 2):
            if (basket[-1] == basket[-2]):
                answer += 2
                basket.pop();
                basket.pop();
    return answer