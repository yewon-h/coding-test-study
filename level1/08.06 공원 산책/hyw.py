def solution(park, routes):
    answer = []
    map = []
    W = len(park[0])
    H = len(park)

    # 방향 좌표 더하기
    direction = {"N": [-1, 0],
                "S": [1, 0],
                "W": [0, -1],
                "E": [0, 1]}
    
    for row, i in enumerate(park): # 시작 좌표 뽑기
        for col,j in enumerate(i):
            if j == "S":
                x = row
                y = col
            
    for i in routes: # 어느 방향으로 얼만큼
        direc, dist = i.split(" ")
        dx , dy = direction[direc]
        
        i = 0
        temp_x, temp_y = x, y # 임시 x, y
        while i < int(dist): # 이동 거리만큼 한칸씩 옮겨가며 조건 확인. 만약 조건을 만족하지 못한다면 break, while문이 끝까지 돌았다면 실제 좌표 업데이트
            temp_x += dx
            temp_y += dy
            if temp_x >= 0 and temp_x <= (H - 1) and temp_y >= 0 and temp_y <= (W - 1) and park[temp_x][temp_y] != "X":
                i += 1
            else:
                break
                
        else:
            x += dx * int(dist)
            y += dy * int(dist)
                
    return [x, y]