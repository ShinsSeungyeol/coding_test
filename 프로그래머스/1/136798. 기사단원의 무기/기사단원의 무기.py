def solution(number, limit, power):
    dp = [0 for i in range(number+1)]
    dp[0] = 0
    dp[1] = 1
    answer = 1
    
    for i in range(2, number+1):
        for j in range(1, int(i ** 0.5)+1):
            if (i % j == 0):
                dp[i] += 2
        else:
            if i == int(i ** 0.5) * int(i ** 0.5):
                dp[i] -= 1
                
        if dp[i] > limit:
            answer += power
        else:
            answer += dp[i]
            
    return answer
            
    