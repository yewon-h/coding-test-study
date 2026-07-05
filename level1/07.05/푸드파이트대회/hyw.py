def solution(food):
    answer = ''
    
    for idx in range(len(food)):
        if food[idx] // 2 >= 1:
            answer +=  str(idx) * (food[idx] // 2)       
        else:
            continue
            
    reverse = answer[::-1]
    
    return answer + '0' + reverse