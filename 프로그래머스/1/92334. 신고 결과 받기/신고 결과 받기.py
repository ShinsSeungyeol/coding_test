def solution(id_list, report, k):
    answer = [0 for id in id_list]
    
    
    set_report = set(report)
    dict_report = {id:'' for id in id_list}

    for r in set_report:
        reporter, reported = r.split()
        dict_report[reported] += reporter + ' '

    for key, value in dict_report.items():
        list_reporter = list(value.split(' '))
        list_reporter.pop()
        
        
        if (len(list_reporter) >= k):
            for reporter in list_reporter:
                answer[id_list.index(reporter)] += 1
        
        
    return answer