def solution(today, terms, privacies):
    answer = []
    t_yyyy, t_mm, t_dd = map(int, today.split('.'));

    for i in range (0, len(terms)):
        ty, term = terms[i].split();
        term = int(term)

        for j in range (0, len(privacies)):
            begin_date, pty = privacies[j].split();
            b_yyyy, b_mm, b_dd = map(int,begin_date.split('.'));

            if (pty == ty):
                b_mm += term;

                if (b_mm > 12):
                    b_yyyy += b_mm // 12;
                    b_mm = b_mm % 12;
                    if (b_mm == 0):
                        b_mm = 12;
                        b_yyyy -= 1;
                if (t_yyyy > b_yyyy):
                    answer.append(j+1);
                elif (t_yyyy == b_yyyy and t_mm > b_mm):
                    answer.append(j+1);
                elif (t_yyyy == b_yyyy and t_mm == b_mm and t_dd >= b_dd):
                    answer.append(j+1);






    return sorted(answer)
