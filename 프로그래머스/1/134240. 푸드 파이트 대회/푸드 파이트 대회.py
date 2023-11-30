def solution(food):
    answer = ''
    
    for i in range(1, len(food)):
        if (int(food[i]) // 2 >= 1):
            answer += str(i) * (int(food[i]) // 2)
    answer += '0'
    answer += answer[0:-1][::-1]
    return answer