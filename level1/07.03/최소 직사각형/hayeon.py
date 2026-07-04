def solution(sizes):
    answer = 0
    temp_list = sizes[0]
    
    for i in range(len(sizes)):
        sizes[i].sort()
        temp_list[0] = max(temp_list[0],sizes[i][0])
        temp_list[1] = max(temp_list[1],sizes[i][1])
        
    answer = temp_list[0] * temp_list[1]
    return answer
