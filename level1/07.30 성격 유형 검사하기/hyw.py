def solution(survey, choices):
    answer = ''
    personality = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    
    for i, j in zip(survey, choices):
        
        if j < 4:
            personality[i[0]] += 4 - j
            
        if j > 4:
            personality[i[1]] += j - 4
            
    i = 0
    keys_list = list(personality.keys())
    
    while i < 8:
        if personality[keys_list[i]] >= personality[keys_list[i+1]]:
            answer += keys_list[i]
            
        else:
            answer += keys_list[i+1]
            
        i += 2
    
    return answer
