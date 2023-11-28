def solution(players, callings):
    dict_ranking = {k:i for i, k in enumerate(players)} # 선수 이름 : 순위
    
        
   

    for i, calling in enumerate(callings):
        ranking_before_calling = dict_ranking[calling] 
        overtaken = players[ranking_before_calling - 1]
        
        dict_ranking[calling], dict_ranking[overtaken] = dict_ranking[overtaken], dict_ranking[calling]
        players[ranking_before_calling], players[ranking_before_calling-1] = players[ranking_before_calling-1], players[ranking_before_calling]

    return players