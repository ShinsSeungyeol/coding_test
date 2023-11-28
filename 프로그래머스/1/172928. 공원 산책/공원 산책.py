def solution(park, routes):
    park = [[park[i][j] for j in range (len(park[i]))] for i in range(len(park))];
    dict_direction = {
        'E': [0, 1],
        'S': [1, 0],
        'N': [-1, 0],
        'W': [0, -1],
    }
    cur = []
    
    for i, row in enumerate(park):
        for j, col in enumerate(row):
            if col == 'S':
                cur = [i, j];       
                
    for i in range(len(routes)):
        direction, n = routes[i].split()
        n = int(n)
        next_h = cur[0]
        next_w = cur[1]
        
        for j in range(n):
            next_h += dict_direction[direction][0]
            next_w += dict_direction[direction][1]
            
            if (next_h < 0 or next_h >= len(park) or next_w < 0 or next_w >= len(park[next_h]) or park[next_h][next_w] == 'X'):
                break;
        else:
            cur = [next_h, next_w]
                
    return cur