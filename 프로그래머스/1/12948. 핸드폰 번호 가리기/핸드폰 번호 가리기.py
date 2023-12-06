def solution(phone_number):
    answer = ['*' for i in phone_number[0:-4]] + list(phone_number[-4:])
    answer = ''.join(answer)
    return answer