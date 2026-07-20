def solution(keymap, targets):
    answer = []
    key_sum = 0
    not_find = 0
    temp_list = []
    for i in targets:
        for j in i:
            for k in keymap:
                kkk = k.find(j)
                if kkk == -1 :
                    kkk = 101
                temp_list.append(kkk)
            
            
            if len(temp_list) == temp_list.count(101):
                not_find = -1
            else:
                key_sum += min(temp_list)
                key_sum += 1
                
            temp_list = []
                
            
        if not_find == -1:
            answer.append(-1)
            not_find = 0
        else:
            answer.append(key_sum)
        
        key_sum = 0
        
            
            
    return answer
