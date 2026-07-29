def solution(board, moves):
    answer = 0
    basket = [] # 담아두기
    
    for i in moves:
        for j in range(len(board[0])): # 보드 크기 n * n
            if board[j][i - 1] != 0: # 빈칸이 아닐 때 바구니에 넣기
                if basket and basket[-1] == board[j][i - 1]: # 전에 담겨있는 인형과 비교해서 터지거나 담거나
                    answer += 2 # 인형 두개씩 터짐
                    del basket[-1] # 바구니에서 삭제
                    board[j][i - 1] = 0  # 보드에서 삭제
                    
                else:
                    basket.append(board[j][i - 1]) # 바구니에 담기만 함
                    board[j][i - 1] = 0  # 보드에서 삭제
                break
            
    return answer 