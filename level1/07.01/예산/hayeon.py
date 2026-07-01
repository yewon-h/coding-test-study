def solution(d, budget):
    answer = 0
    d.sort()
    
    sum_v = 0
    
    for i , v in enumerate(d):
        sum_v += v
        answer = i
        
        if sum_v == budget:
            answer += 1
            return answer
            
        elif sum_v > budget:
            return answer
    
    return answer + 1



#return 하면 반복문은 자동으로 끝난다
#왜냐하면 함수 자체가 종료되기 때문이다.
#마지막 + 1 은 끝까지 다 돌았을 때 index 번호가 하나 비어버리기 때문이다 
# answer + 1 대신  len(d) 해도 상관 없을 듯?
