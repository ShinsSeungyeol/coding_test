def solution(n, arr1, arr2):
    board = [''.join(to_board(n, arr1[i] | arr2[i]))  for i in range(n)]
    
    return board

def to_board (n, val):
    board = ['0'] * n
    
    idx = n-1
    while (idx >= 0):
        remain = val % 2
        
        if remain == 1:
            board[idx] = '#'
        else:
            board[idx] = ' '
        val //= 2
        idx -= 1
    
    return board
    