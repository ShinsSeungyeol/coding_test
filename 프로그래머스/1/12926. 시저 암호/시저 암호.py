def solution(s, n):
    answer = ''
    
    for c in s:
        if c == ' ':
            answer += c
        elif 65 <= ord(c) <= 90:
            answer += chr((ord(c) + n - 65) % 26 + 65)
        elif 97 <= ord(c) <= 127:
            answer += chr((ord(c) + n - 97) % 26 + 97)
    return answer