def solution(n):
    answer = 0
    
    for i in range(2, n+1):
        if is_prime(i):
            answer += 1
    return answer

def is_prime(n):
    i_sqrt = int(n ** 0.5)
    for i in range(2, i_sqrt + 1):
        if n % i == 0:
            return False
    return True
    

