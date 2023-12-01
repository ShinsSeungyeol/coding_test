def solution(a, b, n):
    # a: 콜라를 받기 위해 주어야 하는 병수
    # b: 개를 가져다 주면 마트가 주는 콜라 병수 
    # n: 상빈이가 가지고 있는 콜라의 병수 
    answer = 0
    while (n >= a):
        send = (n // a) * a
        receive = (n // a) * b
        
        n -= send
        n += receive
        answer += receive
        

    return answer