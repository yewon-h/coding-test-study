def solution(s):
    answer = ''
    switch_num = 0

    for i in s:
        
# switch_num이 0 이면 대문자 , 아니면 소문자로 answer 안에다가 넣기
        if switch_num == 0 :
            answer += i.upper()
        else:
            answer += i.lower()
            
            
# switch_num이 공백을 만나거나 0이 아니면 다시 0으로 돌려주기
            
        if i == " " or switch_num != 0 :
            switch_num = 0
        else:
            switch_num = 1

    return answer
