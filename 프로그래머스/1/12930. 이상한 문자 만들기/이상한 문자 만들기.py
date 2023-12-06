def solution(s):
    list_s = list(s.split(' '))
    for j, word in enumerate(list_s):
        weired = ''
        for i,c in enumerate(word):
            if i % 2 == 0:
                weired += c.upper()
            else:
                weired += c.lower()
        list_s[j] = weired
    

                
    return (" ").join(list_s)