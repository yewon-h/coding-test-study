def solution(park, routes):
    answer = []
    좌표 = {
        "x" : 0,
        "y" : 0
    }
    
    공원가로길이 = len(park[0])
    공원세로길이 = len(park)
    함정 = []
    
    def E_fnc(얼만큼):
        임시_x = 좌표["x"]
        y = 좌표["y"]
        
        for i in range(얼만큼):
            임시_x += 1
            
            if 임시_x >= 공원가로길이:
                return 좌표["x"]
            else:
                for j in 함정:
                    if y == j["y"] and 임시_x == j["x"]:
                        return 좌표["x"]
        else:
            print(f"{좌표}, {어디로}방향으로 {얼만큼}이동")
            return 임시_x
    
    def W_fnc(얼만큼):
        임시_x = 좌표['x']
        y = 좌표['y']
        
        for i in range(얼만큼):
            임시_x -= 1
            
            if 임시_x < 0:
                return 좌표["x"]
            else:
                for j in 함정:
                    if y == j['y'] and 임시_x == j['x']:
                        return 좌표["x"]
        else:
            print(f"{좌표}, {어디로}방향으로 {얼만큼}이동")
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
            print(f"{좌표}, {어디로}방향으로 {얼만큼}이동")
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
                    
                    

    for i,v in enumerate(park):
        for k,j in enumerate(v):
            if j == "S":
                좌표["x"] = k
                좌표["y"] = i
                
            if j == "X":
                함정.append({"x":k,"y":i})
                
    print(f"{좌표} 초기 좌표")
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
