def solution(n):
    answer = 0
    list_n = list(str(n))
    list_n = sorted(list_n, reverse=True)
    answer = int("".join(list_n))
    return answer