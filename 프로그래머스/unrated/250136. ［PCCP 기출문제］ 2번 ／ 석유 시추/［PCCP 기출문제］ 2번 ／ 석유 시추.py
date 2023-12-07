def solution(land):
    dir = [[0, -1],[0, 1],[1, 0],[-1, 0]]
    w, h = len(land[0]), len(land)
    total_amount = [0 for i in range(w)]
    visited = [[False for i in range(w)] for j in range(h)]

    for j in range(w):
        for i in range(h):
            if land[i][j] == 1 and (not visited[i][j]):
                amount = 0
                min_j = j 
                max_j = j
                next = [[i, j]]
                visited[i][j] = True
                
                while  len(next) != 0:
                    n_i = next[-1][0]
                    n_j = next[-1][1]
                    min_j = min(min_j, n_j)
                    max_j = max(max_j, n_j)
                    
                    next.pop();
                    amount += 1
                    
                    for d in dir:
                        if (0 <= n_i + d[0] < h) and (0 <= n_j + d[1] < w) and (land[n_i + d[0]][n_j + d[1]] == 1) and (not visited[n_i + d[0]][n_j + d[1]]):
                            next.append([n_i + d[0], n_j + d[1]])
                            visited[n_i + d[0]][n_j + d[1]] = True  
                            
                for k in range(min_j, max_j+1):
                    total_amount[k] += amount
            

    return max(total_amount)