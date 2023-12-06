def solution(a, b):
    begin, end = min(a, b), max(a, b)+1
    answer = sum([i for i in range(begin, end)])
    return answer