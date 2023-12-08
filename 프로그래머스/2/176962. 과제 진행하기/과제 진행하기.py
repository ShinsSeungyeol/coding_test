def solution(plans):
    answer = []
    yet = []
    plans = sorted(plans, key=lambda x : x[1])
    print(plans)
    
    for i, plan in enumerate(plans):
        name = plan[0]
        hhmm = plan[1]
        taken = int(plan[2])
        
        hh, mm = map(int, hhmm.split(':'))
        
        start = 60 * hh + mm
        
        comple_minutes = start + taken
        
        
        if i < len(plans) - 1: 
            next_hh, next_mm = map(int, plans[i+1][1].split(':'))
            next_minutes = 60 * next_hh + next_mm
        
            rest_minutes = next_minutes - comple_minutes
            if (rest_minutes >= 0):
                answer.append(name)
            
                while rest_minutes > 0 and len(yet) != 0:
                    work = yet.pop()
                    yet_name, yet_minutes = work[0], work[1]
               
                    if rest_minutes < yet_minutes:
                        yet.append([yet_name, yet_minutes - rest_minutes])
                        rest_minutes = 0
                    else:
                        answer.append(yet_name)
                        rest_minutes -= yet_minutes
            else:
                yet.append([name, comple_minutes - next_minutes]);
                
        else:
            answer.append(name)
            answer += reversed([work[0] for work in yet])
            
    return answer




    