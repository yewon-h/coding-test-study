def solution(t, p):
    answer = 0
    time = len(t) - (len(p) - 1)
    
    for i in range(time):
        if int(t[i:i+len(p)]) <= int(p):
            answer += 1
        else:
            continue
    
    return answer