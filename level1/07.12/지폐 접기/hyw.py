def solution(wallet, bill):
    
    answer = 0
    max_b = max(bill)
    min_b = min(bill)  
    max_w = max(wallet)
    min_w = min(wallet)
    
    while max_b > max_w or min_b > min_w:
        max_b = max_b // 2
        max_b, min_b = max(max_b, min_b), min(max_b, min_b)
        answer += 1
    
    return answer