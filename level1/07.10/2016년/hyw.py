def solution(a, b):
    
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    total_num = 0
    
    for i in range(a-1):
        total_num += month_days[i]
    
    total_num += b
        
    return week[(total_num % 7)]