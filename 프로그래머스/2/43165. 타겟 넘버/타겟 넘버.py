
def solution(numbers, target):
    answer = getNumberOfCases(0, 0, numbers, target)
    return answer

def getNumberOfCases(val, idx, numbers, target):
    if idx == len(numbers):
        if val == target:
            return 1
        else:
            return 0
    
    return getNumberOfCases(val+numbers[idx], idx+1, numbers, target) + getNumberOfCases(val-numbers[idx], idx+1, numbers, target)
        