def solution(numbers):
    answer = []
    
    for i, value1 in enumerate(numbers):
        for j, value2 in enumerate(numbers[i+1:]):
            answer.append(value1 + value2)
            
    answer = sorted(set(answer))
    return answer