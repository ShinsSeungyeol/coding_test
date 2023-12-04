def solution(n):
    answer = 0
    base_three = ''
    
    while n > 0 :
        base_three = str(n % 3) + base_three
        n = n // 3
 
    base_three = base_three[::-1]
    
    for i in range(len(base_three)):
        answer += int(3 ** i) * int(base_three[len(base_three)-i-1])
    

    return answer