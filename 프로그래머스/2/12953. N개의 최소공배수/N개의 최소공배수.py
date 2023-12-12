def solution(arr):
    answer = 0
    common_multiple = arr[0]
    divisor = get_divisor(arr[0])
    
    for i in range(1, len(arr)):
        common_divisor = list(set.intersection(get_divisor(common_multiple), get_divisor(arr[i])))
        common_multiple *= arr[i]
        common_multiple //= max(common_divisor)
      
        
    return common_multiple


def get_divisor(num):
    divisor = []
    sqrt_num = int((num ** 0.5))
    
    if num <= 3:
        divisor.append(1)
        divisor.append(num)
    else:
        for i in range(1, sqrt_num+1):
            if num % i == 0:
                divisor.append(i)
                divisor.append(num // i)
    
    return set(divisor)