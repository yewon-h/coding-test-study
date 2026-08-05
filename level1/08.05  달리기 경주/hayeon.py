# 딕셔너리로 각 선수들 순위를 기록해주고
# playsers 에서 리스트 형식으로 순위를 계속 업데이트 해준다.
# 딕셔너리에서 순위는 playsers의 인덱스 번호랑 동일하다. --> 바뀔때마다 계속 업데이트 시킴
# 리스트에서 바로 .index()함수 써서 사용하면 시간이 진짜 개 오래걸린다.
# 제법 성장했다.

def solution(players, callings):
    answer = []
    p_rank = {}
    
    for i, v in enumerate(players):
        p_rank[v] = i
    
    # a   = 앞지러서 호명된 사람
    # a_i = a 의 현재 순위
    # b   = a 한테 제쳐질 사람, a 보다 앞에 있는사람
    # b_i = b의 현재 순위 
    for a in callings:  # 호명 된 사람을 불러온다.
        a_i = p_rank[a]   # 그 사람의 현재 순위를 변수에 저장한다
        b_i = a_i - 1      # 그리고 그 앞사람 순위를 변수에 저장한다
        b = players[b_i]   #  playsers 리스트에서 a 앞에 있는 사람을 저장한다.
        
        players[a_i], players[b_i] = players[b_i], players[a_i]  # 리스트 안에서 그 둘의 위치를 스왑한다.
        
        p_rank[a] = b_i   # 딕셔너리값도 업데이트 해준다
        p_rank[b] = a_i   # 똑같이 업데이트 해준다.

      # 위에 작업이 끝나면 한 번 호명될 때 마다 players리스트와, p_rank의 딕셔너리 값이 계속 업데이트된다.
    return players

