import math

###########################################
# 시간초과
###########################################

def solution(n):
    answer = 0
    prime = 0
    i = 2
    
    while i <= n:
        count = 0
        j = 2
        
        while j <= math.sqrt(i):
            if i % j == 0:
                break
            j += 1
            
        else:
            answer += 1
            
        i += 1
    return answer

###########################################
# 아이디어 못떠올림 제미나이한테 배수 지우는 방법으로 접근하라는 대답 들음
# n 이하 숫자 리스트 만들고 2의 배수, 3의 배수 순서대로 0으로 만들어버림
# 0 아닌 숫자 개수 세서 반환 
# 계속 시간 초과 떠서 푸는데 시간 진짜 엄청 썼어
###########################################
import math

def solution(n):
    answer = 0
    
    prime_check = [i for i in range(n + 1)]
    prime_check[1] = 0
    
    for i in prime_check:
        if i != 0:
            for j in range(i*2 , n+1, i):
                prime_check[j] = 0
                
    
    answer = len([x for x in prime_check if x != 0])
        
        
        
    return answer