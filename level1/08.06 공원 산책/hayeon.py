# S와 함정의 좌표를 딕셔너리형태로받는다.
def solution(park, routes):
    answer = []
    # S 좌표
    좌표 = {  
        "x" : 0,
        "y" : 0
    }
    
    공원가로길이 = len(park[0])
    공원세로길이 = len(park)
    # 함정은 개수가 많아 2차원 배열안에 딕셔너리로 넣는 방식을 택한다.
    # ex) [ ["x" : 3,"y" : 4], ------------]
    함정 = []


    # 어느 방향으로 얼만큼 이동하는지 확인 후 동서남북을 각각 함수로 만들어 조건을 체크한다.
    # 조건에 맞지 않으면 원래 좌표를 반환하고 모든 조건에 충족한다면 이동한 좌표를 반환한다.
    def E_fnc(얼만큼):
        임시_x = 좌표["x"]
        y = 좌표["y"]
        
        for i in range(얼만큼):  # 한 칸 씩 옮겨주기 위해 반복 횟수를 정해준다.
            임시_x += 1   # E 방향이기 때문에 +1 한 칸씩 옮겨준다.
            
            if 임시_x >= 공원가로길이:   # 공원가로길이를 넘어 간다면
                return 좌표["x"]        # 원래 좌표를 반환 (이동X), 즉시 반복문이 끝난다.
            else:   # 공원길이를 넘어가지 않는다면
                for j in 함정:  # 모든 함정을 다 가져와 비교한다.
                    if y == j["y"] and 임시_x == j["x"]:  # 함정의 y 좌표와 같고, 이동한 x좌표가 같아 장애물을 만났다면
                        return 좌표["x"]   # 원래 좌표를 반환(이동x)
        else:  # 위에 두 조건을 다 만족시켜서 이동이 끝났다면
            return 임시_x  # 이동한 좌표를 반환한다.
    
    def W_fnc(얼만큼):
        임시_x = 좌표['x']
        y = 좌표['y']
        
        for i in range(얼만큼):
            임시_x -= 1 # 서쪽으로 갔기 때문에 -1 칸 씩 해준다.
            
            if 임시_x < 0: # 서쪽의 끝은 0 이기 때문에 0 보다 작아지면 공원을 나간거다.
                return 좌표["x"]
            else:
                for j in 함정:
                    if y == j['y'] and 임시_x == j['x']:
                        return 좌표["x"]
        else:
            return 임시_x
        
    def S_fnc(얼만큼):
        x = 좌표['x']
        임시_y = 좌표['y']
        
        for i in range(얼만큼):
            임시_y += 1
            
            if 임시_y >= 공원세로길이:
                return 좌표['y']
            else:
                for j in 함정:
                    if x == j['x'] and 임시_y == j['y']:
                        return 좌표['y']
        else:
            return 임시_y
        
    def N_fnc(얼만큼):
        x = 좌표['x']
        임시_y = 좌표['y']
            
        for i in range(얼만큼):
            임시_y -= 1
                
            if 임시_y < 0:
                return 좌표['y']
            else:
                for j in 함정:
                    if x == j['x'] and 임시_y == j['y']:
                        return 좌표['y']
        else:
            return 임시_y
                    
                    
# 공원에서 산책 출발지, 함정의 좌표를 찾아서 넣어준다.
    for i,v in enumerate(park):
        for k,j in enumerate(v):
            if j == "S":
                좌표["x"] = k
                좌표["y"] = i
                
            if j == "X":
                함정.append({"x":k,"y":i})



# 이제 이동을 시켜준다. 끝.
    for i in routes:
        어디로 = i.split()[0]
        얼만큼 = int(i.split()[1])

        if 어디로 == "E":
            좌표["x"] = E_fnc(얼만큼)

        elif 어디로 == "W":
            좌표["x"] = W_fnc(얼만큼)

        elif 어디로 == "S":
            좌표["y"] = S_fnc(얼만큼)

        else:
            좌표["y"] = N_fnc(얼만큼)

    answer.append(좌표["y"])
    answer.append(좌표["x"])
    return answer
