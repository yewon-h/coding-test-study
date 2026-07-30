def solution(survey, choices):
    answer = ''
    
    score = {
        "R" : 0,
        "T" : 0,
        "C" : 0,
        "F" : 0,
        "J" : 0,
        "M" : 0,
        "A" : 0,
        "N" : 0
    }
    
    for i in range(len(choices)):
        if choices[i] == 4:
            continue
            
        elif choices[i] < 4:
            score[survey[i][0]] += 4 - choices[i]
        
        elif choices[i] > 4:
            score[survey[i][1]] += choices[i] - 4
                
    keys_list =list(score.keys())
    
    for i in range(0,8,2):
        if score[keys_list[i]] >= score[keys_list[i+1]]:
            answer += keys_list[i]
        else:
            answer += keys_list[i+1]
            
    return answer
