def solution(price, money, count):
    answer = 0
    need = 0
    
    for i in range(1, count+1):
        need += i * price
    
    
    answer = need - money
    answer = answer if answer > 0 else 0

    return answer