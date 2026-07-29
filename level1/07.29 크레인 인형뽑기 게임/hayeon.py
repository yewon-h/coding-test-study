def solution(board, moves):
    answer = 0
    temp_list = []
    
    for i in moves:
        for j in board:
            if j[i-1] != 0 :
                temp_object = j[i-1]
                j[i-1] = 0
        
                if len(temp_list) > 0 and temp_list[-1] == temp_object:
                    temp_list.pop()
                    answer += 2
        
                else:
                    temp_list.append(temp_object)
                break
    return answer
