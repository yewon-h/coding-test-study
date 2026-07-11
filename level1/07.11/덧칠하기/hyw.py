def solution(n, m, section):
    answer = 0
    start = 0
    
    for i in section:
        
        if i > start:
            answer += 1
            start = i + m - 1
        
    return answer