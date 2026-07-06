def solution(k, score):
    answer = []
    top_k = []
    
    for i in score:
        top_k.append(i)
        top_k = sorted(top_k, reverse = True)[:k]
        
        answer.append(min(top_k))
        
    return answer