def solution(numbers, hand):
    answer = ''
    keyboard = [[3, 1], [0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2,2]]
    left_hand_pos, right_hand_pos = [3, 0], [3, 2]

    for n in numbers:
        y, x = keyboard[n][0], keyboard[n][1]
        if n % 3 == 1:
            dir = 'L'
        elif n >= 3 and n % 3 == 0:
            dir = 'R'
        else:
            left_distance = abs(left_hand_pos[0] - y) + abs(left_hand_pos[1] - x)
            right_distance = abs(right_hand_pos[0] - y) + abs(right_hand_pos[1] - x)
        
            if left_distance < right_distance:
                dir = 'L'
            elif right_distance < left_distance:
                dir= 'R'
            else:
                dir = 'L' if hand == 'left' else 'R'
            
        if dir == 'L':
            left_hand_pos = [y, x]
        else:
            right_hand_pos = [y, x]
        
        answer += dir
    
    return answer