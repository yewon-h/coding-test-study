def solution(dartResult):
    
    dartResult = dartResult.replace('10', 't')
    # 마지막에 다 더할거니까 첫 시작을 무조건 0으로 넣어버림 첫 점수 + 스타상받았을 때 하나 앞 *2할 때 인덱스에러 안나게
    scores = []
    score = 0
    
    for i in dartResult:
        if i == 't': # 첫 점수가 10일때 따로 처리
            scores.append(score) # 첫 점수일 때 0들어가고 이후에는 다음 점수 만날때 이전 [점수 + sdt/*#] 계산결과 넣음
            score = 10 # 앞으로 계산해나갈 점수, score안에서 모두 연산되고 다음 점수 만나면 scores안에 원소로 들어감
            
        if i.isdigit(): # 입력값이 숫자인가?
            scores.append(score)
            score = int(i)
            
        if i == 'D':
            score = score**2
            
        if i == 'T':
            score = score**3
            
        if i == '*':
            score = score * 2
            scores[-1] = scores[-1] * 2
            
        if i == '#':
            score = -score
            
    scores.append(score)
    
    return sum(scores)