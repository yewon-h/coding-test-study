def solution(schedules, timelogs, startday):
    answer = 0
    temp = 0
    
    def fnc_con_min(time):
        total_min = (time // 100)*60 + time % 100
        return total_min
    
    
    for k,j in enumerate(timelogs):
        for i,v in enumerate(j):
            if (i+startday) % 7 < 6 and (i+startday) % 7 != 0 : # 평일이면
                if fnc_con_min(v) > fnc_con_min(schedules[k])+10: # 지각했으면
                    break # 탈락

        else:
            answer += 1 # 끝까지 성공했으면 상품 당첨
            
    return answer
