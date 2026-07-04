def solution(s):
    answer = []
    for i in range(len(s)):
        print(s.rfind(s[i],0,i),s[i])
        if s.rfind(s[i],0,i) == -1:
            answer.append(-1)
        else:
            answer.append(i-s.rfind(s[i],0,i))
    
    
    return answer
