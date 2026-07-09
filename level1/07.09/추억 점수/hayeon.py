def solution(name, yearning, photo):
    answer = []
    temp_sum = 0
    
    
    for i in photo:
        for j in range(len(name)):
            
            if name[j] in i :
                temp_sum += yearning[j]
            
        answer.append(temp_sum)
        temp_sum = 0
            
    return answer


