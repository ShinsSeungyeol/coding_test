def solution(book_time):
    room = []
    
    book_time = sorted(book_time, key=lambda x: (x[0], x[1]))
    room.append(book_time[0])
    
    for i in range(1, len(book_time)):
        for j in range(0, len(room)):
            i_room_end_hh, i_room_end_mm = map(int, room[j][1].split(':'))
            i_clean_time = 10
            
            i_room_end_mm = i_room_end_mm + i_clean_time

            if i_room_end_mm >= 60:
                i_room_end_hh += 1
                i_room_end_mm %= 60
        
            room_clear_time = str(i_room_end_hh).zfill(2) + ':' + str(i_room_end_mm).zfill(2)
            
                            
            if room_clear_time <= book_time[i][0]:
                room[j] = book_time[i]
                break
        else:
            room.append(book_time[i])
    
    return len(room)