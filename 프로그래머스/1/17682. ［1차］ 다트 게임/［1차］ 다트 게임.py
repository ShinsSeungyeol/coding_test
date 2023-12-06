import re

def solution(dartResult):
    operator = {
        'S': '**1',
        'D': '**2',
        'T': '**3',
        '#': '*(-1)',
        '*': '*2'
    }

    exp = ''
    score = []
    for i, c in enumerate(dartResult):
        if c in operator:
            if c == '*':
                score[-1] *= 2
            exp += operator[c]
        else:
            if dartResult[i-1] in operator:
                score.append(eval(exp) if len(exp) != 0  else 0)
                exp = c
            else:
                exp += c
    else:
        score.append(eval(exp))
            
    return sum(score)