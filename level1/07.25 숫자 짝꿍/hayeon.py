def solution(X, Y):
    answer = ''
  
    str(X) # 문자열 count를 위한 형 변환
    str(Y) # 문자열 count를 위한 형 변환
  
    for i in range(10): #   0 ~ 9 까지 각 X, Y에 몇개 씩 들어잇는지 확인해준다.
        num_X = X.count(str(i)) 
        num_Y = Y.count(str(i))
        answer += min(num_X,num_Y) * str(i) # 그리고 가장 적게 들어있는 수 만큼 곱해서 문자열에 더해준다.( 이 과정에서 그냥 리스트에 넣어도 상관 없었을 듯 하다)
    
    temp = sorted(answer, reverse = True)  # 문자열을 sorted 하면 리스트 형태로 반환된다. print 찎어보고 알았따
    answer = "" # 다시 answer에 주워담아서 return 할거라 빈 문자열로 초기화시켜준다
    if temp == []:  # 일치되는게 없을 때
        return "-1"  # -1 반환하기
    else:     # 뭐라도 들어 있다면
        for i in temp: # 이미 내림차순으로 정리된 수를 차곡차곡 합쳐준다.
            if i  == "0" and answer == "": # 하지만 내림차순 가장 첫번째, 즉 일치하는 숫자가 0 밖에 없는경우, 처음 받는 숫자가 0 이기 때문에 answer이 공백인 경우는 0을 반환한다.
                return "0"
            else: # temp 안에 0 말고 다른 숫자가 있다면
                answer += i  # 차곡 차곡 더해준다
    
    return answer
