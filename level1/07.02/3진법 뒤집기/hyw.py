def solution(n):
    answer = 0
    conv3 = ''
    left = 0
    
    while n >= 3:
        conv3 += str(n % 3)
        n = n // 3
        
    conv3 += str(n)
    
    for i in range(1, len(conv3)+1):
        answer += int(conv3[-i]) * (3**(i-1))
    
    
    return answer