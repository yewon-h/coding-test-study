def solution(schedules, timelogs, startday):
    answer = 0
    # while로 일주일 반복하되 6, 7에서는 지각처리 안함
    # 시간은 그냥 싹 분으로 변환하여 비교
    # 각 사람 한명한명 순차적으로 살펴보기
    
    for idx, schedule in enumerate(schedules):
        schedule_min = (schedule // 100) * 60 + (schedule % 100)
        time_log = tiamelogs[idx]
        day = startday
        
        i = 1
        success = 0
        while i <= 7:

            if day == 6 or day == 7:
                i += 1
                day = (day % 7 )+ 1
                continue
                
            timelogs_min = (time_log[i - 1] // 100) * 60 + (time_log[i - 1] % 100)
            
            if timelogs_min <= schedule_min + 10:
                success += 1
                
            day = (day % 7 )+ 1
            i += 1
            
        if success == 5:
            answer += 1
    
    
    return answer