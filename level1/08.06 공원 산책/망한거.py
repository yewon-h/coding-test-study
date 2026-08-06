# 망함
def solution(park, routes):
    answer = []
    좌표 = {
        "x" : 0,
        "y" : 0
    }
    
    공원가로길이 = len(park[0])
    공원세로길이 = len(park)
    함정 = []
        
    def 이동(a,b,c):
        if a == "E":
            c = 좌표["x"]
            c += b
            
        elif a == "W":
            c = 좌표["x"]
            c -= b
            
        elif a == "S":
            c = 좌표['y']
            c += b
            
        else:
            c = 좌표['y']
            c -= b
        return c
    
        def 실제이동(a,b,c):
            if a == "E":
                좌표["x"] += b
            elif a == "W":
                좌표["x"] -= b
            elif a == "S":
                좌표['y'] += b
            else:
                좌표['y'] -= b
            return 좌표
    
    def 공원길이제한(a):
        if a >= 공원세로길이:
            return "공원을 넘어감"
        elif a >= 공원가로길이:
            return "공원을 넘어감"
        elif a < 0:
            return "공원을 넘어감"
        elif a < 0:
            return "공원을 넘어감"
        
        
        
    for i,v in enumerate(park):
        for k,j in enumerate(v):
            if j == "S":
                좌표["x"] = k
                좌표["y"] = i
                
            if j == "X":
                함정.append({"x":k,"y":i})
    
    for i in routes:
        temp = i.split()
        어디로 = temp[0]
        얼만큼 = int(temp[1])
        
        if 공원길이제한(이동(어디로,얼만큼,좌표)) == "공원을 넘어감":
            break
        else:
            
            for i in 함정:
                if 어디로 == "E" and 이동(어디로,얼만큼,좌표) > i['x']:
                    continue
                elif 어디로 == "W" and 이동(어디로,얼만큼,좌표) < i['x']:
                    continue
                elif 어디로 == "S" and 이동(어디로,얼만큼,좌표) > i['y']:
                    continue
                elif 어디로 == 'N' and 이동(어디로,얼만큼,좌표) < i['y']:
                    continue
                break
    
    좌표 = 이동(어디로,얼만큼,좌표)
            
    return answer
