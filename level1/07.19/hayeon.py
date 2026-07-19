def solution(s):
    answer = 0
    i = 0 # 인덱스 고정 값
    temp_list = [] # 잘라낸 문자열 담는 변수
    
    while len(s) > 0: # s에서 단어분리시켜서 없애버리는게 목표
        j = 1 # 처음 시작하는 단어 개수 1 인 이유는 처음 시작하면서 동시에 카운팅 되기 떄문
        k = 0 # 시작하는 단어와 다른 단어 개수
        l = s[i] # 처음 시작하는 단어랑 계속 비교하기 때문에 그냥 고정해버린다 
        
        while j != k: 
            if len(s) == 1: # s문자열이 하나 남았을 때 예외처리
                k = 1 # 반복문을 끝내준다
            else:
                i += 1 # index 번호를 늘려 검사한다
                
                if l == s[i]: # 다음에 오는 단어가 같으면
                    j += 1
                else:  # 다음에 오는 단어가 다르면
                    k += 1
                    
            if len(s) == i +1: # 문자열 끝까지 도달했는데 j 랑 k 개수가 달랐을 때 예외처리 ex - 'aaa'
                j = k # 반복문을 끝낸다
                
                
        if len(s) > 1 :        
            temp_list.append(s[:i+1]) #검사한 문자열 보관
            s = s[i+1:] # 검사한 문자열 잘라내기
            i = 0 # 인덱번호 초기화
            
        elif len(s) == 1: # 마찬가지로 문자열이 하나 있을 떄 예외처리 해준다
            temp_list.append(s)
            s = "" #첫 번째 반복문에 들어가지 않기 위해 공백을 넣어서 문자열 길이를 0으로 만들어준.
        
    answer = len(temp_list)
        
    return answer
