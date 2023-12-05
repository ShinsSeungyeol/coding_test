def solution(array, commands):
    answer = []
    
    for command in commands:
        begin, end, target = command[0]-1, command[1], command[2]-1
        
        sub_array = sorted(array[begin:end])
    
        answer.append(sub_array[target])
    return answer