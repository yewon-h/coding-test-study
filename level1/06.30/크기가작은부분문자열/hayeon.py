def solution(t, p):
    answer = 0
    end = len(t) - len(p)
    
    for i in range(end +1):
        num=int(t[i:len(p)+i])
        if num <= int(p):
                answer += 1
    return answer
