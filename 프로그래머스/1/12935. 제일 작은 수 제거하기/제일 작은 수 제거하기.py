def solution(arr):
    min_val = min(arr)
    arr.remove(min_val)
    arr = [-1] if len(arr) == 0 else arr
    return arr