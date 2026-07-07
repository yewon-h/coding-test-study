def solution(a, b, n):
    answer = 0
    left = 0
    
    while n >= a:
        left += n % a
        n -= left
        n = (n // a) * b
        answer += n
        n += left
        left = 0
    
    return answer