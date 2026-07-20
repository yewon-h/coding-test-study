def solution(lottos, win_nums):
    answer = []
    high = 0
    low = 0
    zero_num = 0
    for i in lottos:
        if i in win_nums:
            high += 1
        elif i == 0:
            zero_num += 1
            
    low = high
    
    if high + zero_num > 7:
        high = 6
    else:
        high = high+zero_num
        
    if high == 0 :
        high = 1
    if low == 0 :
        low = 1
    
    answer = [7-high,7-low]
    
    return answer
