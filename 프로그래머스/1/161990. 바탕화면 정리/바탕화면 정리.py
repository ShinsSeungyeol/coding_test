def solution(wallpaper):
    # 빈칸은 . 파일이 있는 칸은 #
    # 시작점 lux, luy 끝점 rdx, rdy 
    answer = []
    
    board = [[wallpaper[i][j] for j in range(len(wallpaper[i]))] for i in range(len(wallpaper))]
    
    min_x, min_y, max_x, max_y = len(wallpaper[0]), len(wallpaper), 0, 0;
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (board[i][j] == '#'):
                min_x = min(min_x, j)
                min_y = min(min_y, i)
                max_x = max(max_x, j)
                max_y = max(max_y, i)
    
    answer = [min_y, min_x, max_y + 1, max_x + 1]
                    
    return answer