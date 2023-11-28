def solution(bandage, health, attacks):
    #bandage: 시전시간, 초당 회복량, 추가 회복량 
    answer = 0
    hp = health;
    bandageTime = 1;
    idx = 0;
    
    for i in range(1, attacks[-1][0] + 1):
        
        if (i == attacks[idx][0]):
            hp -= attacks[idx][1];
            bandageTime = 1;
            idx += 1;
    
        elif (hp < health):
            hp = hp + bandage[1] if hp + bandage[1]  <= health else health;
            
            if (bandageTime >= bandage[0]):
                hp = hp + bandage[2] if  hp + bandage[2] <= health else health;
            bandageTime += 1;
            
        if (hp <= 0):
            break;
    else:
        answer = hp
    
    if hp <= 0:
        answer = -1
        
        
    return answer