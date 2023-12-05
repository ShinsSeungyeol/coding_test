def solution(N, stages):
    answer = []
    fail_rate = {i : 0 for i in range(N)} #i stage 실패율
    
    cnt_of_total_users = len(stages)
    for i in range(N):
        cnt_of_fail_users =  stages.count(i+1)
        
        if cnt_of_total_users != 0:   
            fail_rate[i] = cnt_of_fail_users / cnt_of_total_users
        else:
            fail_rate[i] = 0
            
        cnt_of_total_users -= cnt_of_fail_users
        
    list_fail_rate = list(fail_rate.items())
    list_fail_rate = sorted(list_fail_rate, key=lambda x : -x[1])
    
    answer = [x[0]+1 for x in (list_fail_rate)]
    return answer