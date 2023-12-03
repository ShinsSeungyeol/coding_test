def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        cnt_measure = calc_cnt_measure(i)
        if cnt_measure % 2 == 0:
            answer += i
        else:
            answer -= i
            
    return answer

def calc_cnt_measure(num):
    cnt_measure = 0
    i_sqrt = int(num**0.5)
    for i in range(1,  i_sqrt+1):
        if num % i == 0:
            cnt_measure += 2
    if i_sqrt * i_sqrt == num:
        cnt_measure -= 1
    return cnt_measure
            