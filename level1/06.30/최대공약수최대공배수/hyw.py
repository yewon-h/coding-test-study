def solution(n, m):
    answer = [0, 0]
    small = min(n, m)
    big = max(n, m)
    
    for i in range(1, small+1):
        if n % i == 0 and m % i == 0:
            answer[0] = i
    
    times = n * m
    for i in range(big, times+1, big):
        if i % small == 0 and i % big == 0:
            answer[1] = i
            break
            
    return answer