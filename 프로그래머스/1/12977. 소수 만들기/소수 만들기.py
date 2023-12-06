def solution(nums):
    answer = 0

    size = len(nums)
    for i in range(size):
        for j in range(i+1, size):
            for k in range(j+1, size):
                if is_prime(nums[i] + nums[j] + nums[k]):
                    answer += 1
    return answer

def is_prime(num):
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True