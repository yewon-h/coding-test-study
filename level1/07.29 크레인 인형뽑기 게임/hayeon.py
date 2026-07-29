def solution(board, moves):
    answer = 0
    temp_list = []
    
    for i in moves:
        for j in board:
            if j[i-1] != 0 :    # 인형이 있을때만
                temp_object = j[i-1]   #  temp_object는 집게로 들고 있는 상태
                j[i-1] = 0   # 인형을 집게로 들고 나가서 0으로 바꿔주기 없는 상태로
        
                if len(temp_list) > 0 and temp_list[-1] == temp_object: # temp_list>0보다 큰 경우에는 아무 것도 없는 예외 처리를 위한, 그리고 집게로 든거랑 바구니 안에 들어있는게 같을 때
                    temp_list.pop() # 바구니 끝에 있는걸 없애주고
                    answer += 2    # 없어진 인형을 더해준다
        
                else:
                    temp_list.append(temp_object)   # 그게 아니라면 바구니에 넣어준다
                break # 그리고 j 열을 싹 찾는 과정을 벗어나고 다음 집게를 가져온다.
    return answer
