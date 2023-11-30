def solution(ingredient):
    # 1: 빵 , 2: 야채, 3: 고기
    answer = 0
    stack = []
    
    for i in range (0, len(ingredient)): 
        stack.append(str(ingredient[i]))
        if stack[-4: ] == list('1231'):
            stack.pop()
            stack.pop()
            stack.pop()
            stack.pop()
            answer += 1
    
    return answer