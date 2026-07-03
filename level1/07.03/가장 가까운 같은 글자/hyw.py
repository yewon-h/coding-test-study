def solution(s):
    answer = []
    check = []
    
    for i in range(len(s)):
        if s[i] not in check:
            answer.append(-1)
            check.append(s[i])
            
        else:
            answer.append(check[::-1].index(s[i]) + 1)
            check.append(s[i])
    
    return answer


