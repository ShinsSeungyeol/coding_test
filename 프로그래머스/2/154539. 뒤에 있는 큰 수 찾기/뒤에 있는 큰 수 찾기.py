
def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    
    for i, num in enumerate(numbers):
        while stack and numbers[stack[-1]] < num:
            answer[stack[-1]] = num
            stack.pop()
        stack.append(i)
        
    
       
    
    return answer 