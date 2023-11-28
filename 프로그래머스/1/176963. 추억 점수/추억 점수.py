def solution(name, yearning, photo):
    answer = []
    dict_yearning = {name[idx]: score for idx, score in enumerate(yearning)};
    
    for photo_element in (photo):
        score = 0
        print(photo_element)
        
        for name_in_photo in (photo_element):
            score += dict_yearning[name_in_photo] if name_in_photo in dict_yearning else 0
        answer.append(score)
    
    
    return answer