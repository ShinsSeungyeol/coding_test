def solution(id_list, report, k):
    answer = [0 for id in id_list]
    
    
    report_set = set(report)
    reported_cnt_list = {id: 0 for id in id_list}

    for r in report_set:
        reporter, reported = r.split(' ')
        reported_cnt_list[reported] += 1
    
    for r in report_set:
        reporter, reported = r.split(' ')
        
        if reported_cnt_list[reported] >= k:
            answer[id_list.index(reporter)] += 1
        
        
        
    return answer