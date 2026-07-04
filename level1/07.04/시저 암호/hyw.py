def solution(s, n):
    answer = ''
    upper = 'abcdefghijklmnopqrstuvwxyz'.upper()
    lower = 'abcdefghijklmnopqrstuvwxyz'
    
    for i in s:
        if i in upper:
            index = (upper.index(i) + n) % 26
            answer += upper[index]
            
        elif i in lower:
            index = (lower.index(i) + n) % 26
            answer += lower[index]
            
        else:
            answer += i
    
    return answer