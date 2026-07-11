def solution(answers):
    answer = []
    
    score1 = 0
    score2 = 0
    score3 = 0
    fnc1 = [1,2,3,4,5]
    fnc2 = [2,1,2,3,2,4,2,5]
    fnc3 = [3,3,1,1,2,2,4,4,5,5]
    fnc1_index = 0
    fnc2_index = 0
    fnc3_index = 0
        
    for i in answers:
            ####################### 1번 학생
            if i == fnc1[fnc1_index]:
                score1 += 1
                
            fnc1_index +=1
            if fnc1_index == 5:
                fnc1_index = 0
            ####################### 2번 학생 
            if i == fnc2[fnc2_index]:
                score2 += 1
                
            fnc2_index += 1
            if fnc2_index == 8:
                fnc2_index = 0
            ######################## 3번 학생
            if i == fnc3[fnc3_index]:
                score3 += 1
                
            fnc3_index += 1
            if fnc3_index == 10:
                fnc3_index = 0
    
    max_score = max(score1,score2,score3)
    
    if max_score == score1:
        answer.append(1)
    if max_score == score2:
        answer.append(2)
    if max_score == score3:
        answer.append(3)
    
    
    return answer
