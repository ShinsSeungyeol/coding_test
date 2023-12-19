def solution(maps):
    answer = []
    visited =[[False for j in range (len(maps[0]))] for i in range(len(maps))] 
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X' and not visited[i][j]:
                stack = []
                stack.append([i, j])
                visited[i][j] = True
                days = int(maps[i][j])
                
                while len(stack) != 0:
                    cur = stack.pop()
                    
                    for k in range(4):
                        n_i, n_j = cur[0] + dy[k], cur[1] + dx[k]
                        if 0 <= n_i < len(maps) and 0 <= n_j < len(maps[0]) and maps[n_i][n_j] != 'X' and not visited[n_i][n_j]:
                            stack.append([n_i, n_j])
                            days += int(maps[n_i][n_j])
                            visited[n_i][n_j] = True
                            
                answer.append(days)
                    
    if len(answer) == 0:
        answer.append(-1)
    else:
        answer =  sorted(answer)

    return answer