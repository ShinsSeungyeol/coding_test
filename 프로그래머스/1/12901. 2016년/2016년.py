def solution(a, b):
    answer = ''
    DAYS = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    WEEK = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    diff_days = 0
    for i in range(1, a):
        diff_days += DAYS[i]
        
    diff_days += b-1
    
    answer = WEEK[diff_days % 7]
    
    return answer
    