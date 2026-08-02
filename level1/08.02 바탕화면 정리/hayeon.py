# "#"이 위치하는 좌표 --> 행 최소 최대, 열 최소 최대를 찾으면 된다.

def solution(wallpaper):
    answer = []
    low = []
    column = []
    
    for i, v in enumerate(wallpaper):
        if "#" in v:  # 일단 행에서 "#"이 존재하는 모든 인덱스를 집어 넣어준다. 사실 그렇게되면 자연스레 low[0]에는 최소 행, low[-1]에는 최대 행이 쌓이지만 직관을 위해 아래 코드를 보면 min,max를 이용했다.
            low.append(i) # "#"이 존재하는 모든 행 번호를 넣어준다
        
        if v.find("#") != -1 :  # 이제 가장 빠른 열을 찾아준다. find 함수는 인덱스 정방향으로 가장 먼저 찾는 인덱스 번호를 반환한다 없으면 -1을 반환해서 아래 min 부분에서 -1이 반환되는것을 막기위해 if문을 사용한다.
            column.append(v.find("#")) # 찾으면 그냥 바로 넣어준다
        
        if v.rfind("#") != -1 : # find함수랑 마찬가지로 인덱스 역방향에서 가장 먼저 찾는 인덱스 번호를 반환하다. 마찬가지로 min값에서 -1이 나올 수 있기 때문에 if문으로 걸러준다
            column.append(v.rfind("#")) # 찾으면 바로 넣어준다.

  # 최솟값들의 좌표
    answer.append(min(low))      
    answer.append(min(column))
  # 최댓값들의 좌표+1을 해주는 이유는 그림을 보면 직관적으로 알 수 있다. +1을 안해주면 모서리 부분 사각형 하나가 빠져버린다.
    answer.append(max(low)+1)
    answer.append(max(column)+1)
    return answer
