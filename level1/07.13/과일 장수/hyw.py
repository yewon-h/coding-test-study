def solution(k, m, score):
    
    score.sort(reverse = True)
    answer = 0
    start = 0
    i = 0
    
    while i  <= len(score)-m :
        box = score[start : start + m]
        answer += box[-1]
        start += m
        i += m
    
    return answer * m