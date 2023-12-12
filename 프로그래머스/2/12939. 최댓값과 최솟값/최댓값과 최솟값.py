def solution(s):
    arr = list(map(int, s.split()))
    min_max = [str(min(arr)), str(max(arr))]


    return ' '.join(min_max)