type_code = {
    'code' : 0,
    'date': 1,
    'maximum': 2,
    'remain': 3
}
def func_filter(ext, val_ext, x):
    return x[type_code[ext]] < val_ext

def solution(data, ext, val_ext, sort_by):
    # data [코드 번호, 제조일, 최대수량, 현재수량
    # ext 어떤 정보를 기준으로 데이터를 뽑아 낼지 
    # val_ext 뽑아낼 정보의 기준값 
    # sort_by 정보를 정렬할 기준이 되는 문자열 
    # data에서 ext 값이 val_ext보다 작은 데이터만 뽑은 후, sort_by에 해당하는 값을 기준으로 오름차순으로 정렬 
    answer = [[]]
    
    filtered_data = [x for x in data if func_filter(ext, val_ext, x)]
                     
    answer = sorted(filtered_data, key=lambda x : x[type_code[sort_by]])
    return answer
                     
                     
