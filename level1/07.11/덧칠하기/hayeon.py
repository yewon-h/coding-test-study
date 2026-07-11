def solution(n, m, section):
    answer = 0
    temp_list=[]
    for i in range(section[0],section[-1]+1):
        temp_list.append(0)
        
    for j in section:
        temp_list[j-section[0]]=1

    for i,v in enumerate(temp_list):
        if v == 1:
            #아래 표현 기억해두기 !!!!!!!!!!!!!!!!!!!!!!
            temp_list[i:i+m]=[0]*m
            ###########################################
            answer +=1

    return answer
