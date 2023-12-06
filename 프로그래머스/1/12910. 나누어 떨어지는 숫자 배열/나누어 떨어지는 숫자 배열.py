def solution(arr, divisor):
    answer = []
    arr = sorted(arr)
    
    answer = [val for val in arr if val % divisor == 0]
    answer = [-1] if len(answer) == 0 else answer
    return answer