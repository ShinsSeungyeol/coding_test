def solution(n):
    answer = 0
    sqrt = int(n**0.5)
    if sqrt * sqrt == n:
        return (sqrt+1) ** 2
    else:
        return -1