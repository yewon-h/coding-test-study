def solution(today, terms, privacies):
    
    answer = []
    
    # {"A": 6달 이런식으로 딕셔너리}
    term_dic = {term.split(" ")[0]: int(term.split(" ")[1]) for term in terms}
    
    today_year, today_month, today_day = map(int, today.split("."))   
    total_today = (today_year*12*28) + (today_month*28) + (today_day)

    for idx, i in enumerate(privacies):

        year, month, day = map(int, i.split()[0].split("."))
        total_privacy = (year * 12 * 28) + (month * 28) + (day)
        Type = i.split()[1]
        
        exp_days = term_dic[Type] * 28
        if exp_days <= (total_today - total_privacy):
            answer.append(idx + 1)
        
        
    return answer
