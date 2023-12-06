def solution(n, m):
    answer = []
    n_divsor_list = calc_divsor_list(n)
    m_divsor_list = calc_divsor_list(m)
    
    common_divsor_list = list(set(n_divsor_list) & set(m_divsor_list))
    answer = [max(common_divsor_list), n*m // max(common_divsor_list)]
    return answer

def calc_divsor_list(num):
    divsor_list = [1, num]
    
    for i in range(2, int(num ** 0.5) + 1):
        if (num % i == 0):
            divsor_list.append(i)
            divsor_list.append(num // i)
            
    return divsor_list
    
    