def solution(answers):
    answer = []
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    for i, answer in enumerate(answers):
        score[0] += int(answer == first[i % 5])
        score[1] += int(answer == second[i % 8])
        score[2] += int(answer == third[i % 10])
    
    answer = [i + 1 for i, s in enumerate(score) if s == max(score)]
    return answer