def solution(k, score):
    answer = []
    temp_list=[]
    
    for i in score:
        temp_list.append(i)
        
        if len(temp_list) > k :
            temp_list.remove(min(temp_list))
            
        answer.append(min(temp_list))

    return answer
