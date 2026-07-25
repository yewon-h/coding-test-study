from collections import Counter # 저번에 찾았던거 한번 써봤다

def solution(X, Y):
    answer = ''
    countX = Counter(X) # Counter({'5': 3, '2': 1})이런식으로 출력됨
    countY = Counter(Y)
    
    # 키 값으로 내림차순 정렬하고 X, Y에서 반복되는 횟수만큼 뽑아서 리스트에 넣기

    for i in sorted(countX.keys(), reverse = True):
        if i in countY.keys(): # 공통으로 key존재하면 min(value)만큼 answer에 더해준다
            # 그냥 너가한것처럼 *로하면 여러번 더해지는지 몰라서 while 써버륌
            # answer += min(countX[i], countY[i]) * i 하기
            k = 0
            while k < min(countX[i], countY[i]): 
                answer += i
                k += 1
                
    if answer == '': # 아무것도 없으면 -1
        return '-1'
    if answer[0] == '0': # 문자열 시작이 0이라면 0 
        return '0'
                
    return answer
