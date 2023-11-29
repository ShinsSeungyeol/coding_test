def solution(s, skip, index):    
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    answer = '';
    for c in s:
        cipher_idx = (ord(c)) - 97;
        i = 0
        while i < index:
            cipher_idx = (cipher_idx + 1) % 26
            if alphabet[(cipher_idx)] in skip:
                i -= 1
            i += 1
        
        answer = answer + alphabet[cipher_idx]
    return answer